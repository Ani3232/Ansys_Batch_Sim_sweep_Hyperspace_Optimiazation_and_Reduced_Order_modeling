# 53126
import logging
import builtins
from termcolor import colored

# Store original print
original_print = builtins.print

# Override print
def print(*args, **kwargs):
    message = " ".join(str(arg) for arg in args)
    logging.info(message)
    original_print(*args, **kwargs)


try:
    import pandas as pd
    import numpy as np
    pd.set_option('display.width', 2000)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    print("[ ",colored("x","green")," ]    Library Importing Succesfull.")
except Exception as e:
    print("[ ",colored("✗","red")," ]    Library Importing Failed:", e)
    raise
    

dataset_path = r"C:\Users\Administrator\Desktop\Thesis\root\dataset\dataset.csv"

try:
    df = pd.read_csv(dataset_path)
    print("[ ",colored("x","green")," ]    Dataset loaded succesfully.")
except Exception as e:
    print("[ ",colored("x","red")," ]    Dataset loading failed:", e)
    

# =============================================================================
#                     ANSYS CONNECTION ESTABLISHMENT
# =============================================================================

try:
    from ansys.workbench.core import connect_workbench
    
    print("[ ",colored("x","green")," ]    connect_workbench imported succesfully.")
except:
    print("[ ",colored("x","red")," ]    connect_workbench importing failed")
    
print("[ ",colored("x","green")," ]    Input Port Number of ansys server: ")
port = input()

try: 
    wb = connect_workbench(port=port)
    print("[ ",colored("x","green")," ]    Workbench connected to port.")
except Exception as e:
    print("[ ",colored("x","red")," ]    Workbench connection Failed:", e)
    exit()

# Import the runner AFTER connection is established
import ansys_runner

# =============================================================================
# HERE COMES THE MAIN ITERATOR
# =============================================================================

FAIL_VALUE = -9999
OUTPUT_MAPPING = {
    'P7': 'Total Deformation Reported Frequency',
    'P8': 'Total Deformation 2 Reported Frequency', 
    'P9': 'Total Deformation 3 Reported Frequency',
    'P10': 'Total Deformation 4 Reported Frequency',
    'P11': 'Directional Deformation Maximum',
    'P12': 'Equivalent Stress Maximum'
}

def extract_numeric_value(value_str):
    """Extract numeric value from string like '159.58 [Hz]'"""
    try:
        return float(value_str.split('[')[0].strip())
    except:
        return FAIL_VALUE

for x in range(len(df)):
    
    # Check if this row needs processing
    if pd.isna(df.loc[x, 'Total Deformation Reported Frequency']):
        
        input_params = {
            "beam_length": df.loc[x, "beam_length"],
            "beam_height": df.loc[x, "beam_height"],
            "beam_width": df.loc[x, "beam_width"],
            "fillet_size": df.loc[x, "fillet_size"]
        }
        
        #print(f"\n[ Processing Row {x} ] Inputs: {input_params}")
        
        # Run Ansys solver
        result = ansys_runner.run_solver(input_params, wb)
        
        # After extracting values, print formatted table
        # After extracting values, print formatted table
        if result.get('success'):
            output_data = result.get('output_parameters', {})
            
            # Collect all values with consistent 20-char formatting
            input_vals = [
                f"{float(input_params['beam_height']):^20.4f}",
                f"{float(input_params['beam_width']):^20.4f}",
                f"{float(input_params['fillet_size']):^20.4f}",
                f"{float(input_params['beam_length']):^20.4f}"
            ]
            
            output_vals = []
            for wb_param, df_col in OUTPUT_MAPPING.items():
                if wb_param in output_data:
                    numeric_val = extract_numeric_value(output_data[wb_param])
                    df.loc[x, df_col] = numeric_val
                    output_vals.append(f"{numeric_val:^20.4f}")
                else:
                    output_vals.append(f"{'N/A':^20}")
            
            # Print header with colored pipe separators
            if x == 0 or x % 10 == 0:
                header = (f"{colored('height', 'cyan'):^20} {colored('|', 'yellow')} "
                        f"{colored('width', 'cyan'):^20} {colored('|', 'yellow')} "
                        f"{colored('fillet', 'cyan'):^20} {colored('|', 'yellow')} "
                        f"{colored('length', 'cyan'):^20} {colored('|', 'yellow')} "
                        f"{colored('Mode1', 'green'):^20} {colored('|', 'yellow')} "
                        f"{colored('Mode2', 'green'):^20} {colored('|', 'yellow')} "
                        f"{colored('Mode3', 'green'):^20} {colored('|', 'yellow')} "
                        f"{colored('Mode4', 'green'):^20} {colored('|', 'yellow')} "
                        f"{colored('Deform', 'magenta'):^20} {colored('|', 'yellow')} "
                        f"{colored('Stress', 'red'):^20}")
                print("\n" + header)
                print(colored("-" * (20*10 + 9*3), 'yellow'))  # 20 cols * 10 + 9 separators * 3 chars
            
            # Print values row
            all_cols = input_vals + output_vals
            values_row = f" {colored('|', 'yellow')} ".join(all_cols)
            print(values_row)
            
            df.to_csv(dataset_path, index=False)
            
        else:
            print(f"[ Row {x} failed: {result.get('error')} ]")
    else:
        print(f"[ Row {x} already processed, skipping ]")

print("[ ",colored("x","green")," ]    Enter 0 to exit workbench: ")
c = input()
if c == "0":
    try:
        wb.exit()
        print("[ ",colored("x","green")," ]    Workbench Exited Succesfully.")
    except:
        print("[ ",colored("x","red")," ]    Workbench Exiting Failed")