
try:
    from termcolor import colored
    print("[ ",colored("x","green")," ]","    Library Importing Succesfull.")
except:
    print(print("[ ","x"," ]","    Library Importing Succesfull."))
try:
    import os
    import sys
    import subprocess 
    import logging
    from datetime import datetime
    import builtins
    print("[ ",colored("x","green")," ]","    Library Importing Succesfull.")
except:
    print("[ ",colored("x","red")," ]","    Library Importing Failed.")
    
    
# creating log directory if it doesn't exists
os.makedirs(r"C:\Users\Administrator\Desktop\Thesis\root\logs", exist_ok=True)


# Create timestamped log file
log_filename = f"C:/Users/Administrator/Desktop/Thesis/root/logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

# Store original print
original_print = builtins.print

# Override print
def print(*args, **kwargs):
    message = " ".join(str(arg) for arg in args)
    logging.info(message)
    original_print(*args, **kwargs)





# Script File Paths
dataset_gen_path    =   r"C:\Users\Administrator\Desktop\Thesis\root\src\dataset_gen.py"
sweep_path          =   r"C:\Users\Administrator\Desktop\Thesis\root\src\sweep.py"
log_clean_path      =   r"C:\Users\Administrator\Desktop\Thesis\self\clean_logs.py"

print("[ ",colored("x","green")," ]","    File paths used: ")
print("[ ",colored("x","green")," ]    ",    dataset_gen_path)

print("[ ",colored("x","green")," ]","    Checking the Dataset validity...")

#process_2 = subprocess.run([sys.executable, log_clean_path])
sys.path.append(dataset_gen_path)
import dataset_gen
sys.path.append(sweep_path)
import sweep