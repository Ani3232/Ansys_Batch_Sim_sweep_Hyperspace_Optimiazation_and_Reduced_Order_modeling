from ansys.workbench.core import connect_workbench

# Connect to your Workbench instance
wb = connect_workbench(port=51753)

script = """
import json

# Get design point
designPoint = Parameters.GetDesignPoint(Name="0")

# Get all parameters
params = Parameters.GetAllParameters()

# Create a list of parameter dictionaries
parameters_list = []
for p in params:
    param_dict = {
        'name': p.Name,
        'value': str(p.Value) if hasattr(p, 'Value') else None,
        'expression': p.Expression if hasattr(p, 'Expression') else None
    }
    parameters_list.append(param_dict)

# Create the complete result
result = {
    'design_point': {
        'name': designPoint.Name,
        'status': str(designPoint.StateOfParameters) if hasattr(designPoint, 'StateOfParameters') else None
    },
    'parameters': parameters_list,
    'total_parameters': len(parameters_list)
}

wb_script_result = json.dumps(result)
"""

result = wb.run_script_string(script)
print(result)

# Now you can easily access any parameter
print(f"\nDesign Point: {result['design_point']['name']}")
print(f"Total parameters: {result['total_parameters']}")
for p in result['parameters']:
    print(f"{p['name']}: {p['value']}")