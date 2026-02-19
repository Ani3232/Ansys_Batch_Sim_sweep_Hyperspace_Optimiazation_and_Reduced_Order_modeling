## This file holds the descriptive documentation of the functions and files



## main.py
 - [ ] Trigger Dataset generation from ansys parameters.csv file and other configuration details.
 - [ ] Load Dataset and trigger sweep.py to run the simulations using the ansys_runner.py and get the results and save the results extracted from the rst files and store them in the database empty columns.
 - [ ] keep logs of the events and prints debug/failure modes etc.

## ansys_runner.py
 - [ ] Launch/attach to ansys session
 - [ ] Open Workbench project
 - [ ] Update parameter values from a row
 - [ ] Trigger geometry update (if required)
 - [ ] Trigger Solve
 - [ ] Detect solve success/failure
 - [ ] Return: path to .rst file, status flag, solve time.
 - [ ] Constraints: 
        - [ ] No dataset writing
        - [ ] No CSV handling
        - [ ] No postprocesing logic
        - [ ] Only "set->solve->return"

## sweep.py
 - [ ] Read parameter combination from loaded dataset
 - [ ] Iterate row by row
 - [ ] For each row:
    - [ ] call ansys_runner.py
    - [ ] call postprocess.py
    - [ ] Return structured results
 - [ ] Handle:
    - [ ] Skip completed run
    - [ ] Retry failed runs (Not Recomended)
    - [ ] COntinuation of solver failure
 - [ ] Output: {
                run_id,
                outputs:{,,,,,,},
                status
                }
 - [ ] Constraints:
    - [ ] No direct file writing
    - [ ] No ANSYS Inernals
    - [ ] Act as loop controller


## postprocess.py
 - [ ] Load .rst file
 - [ ] Frequency Seperation ratio
 - [ ] Max Stress
 - [ ] Max Displacement
 - [ ] Any target KPI
 - [ ] Return structured numeric dictionary
        {
        f1,
        f2,
        f_ratio,
        stress_max,
        disp_max
        }
 - [ ] Constraints: 
        - [ ] No solver execution
        - [ ] No dataset writing
        - [ ] No parameter modification
        - [ ] Just Read->Extract->Return



## dataset_gen.py
 - [ ] Generate datset from ansys's parameter.csv
 - [ ] generate the dataframe and structure for the csv
 - [ ] Assign run ID
 - [ ] Append results from sweep
 - [ ] Update status columns
        - [ ] pending
        - [ ] completed
        - [ ] failed
 - [ ] Save updated dataset safely
 - [ ] Timestamp logging for each run
 - [ ] Ensure atomic writes (prevents curruption)
 - [ ] Constraints:
        - [ ] No Ansys Control
        - [ ] No Postprocessing


## Ansys Details

Ansys 2024 R1
pyansys modules version used:



Package                                     |      Version
--------------------------------------------|--------------------
ansys-api-mechanical                        |       0.1.2
ansys-api-platform-instancemanagement       |       1.1.3
ansys-api-workbench                         |       0.2.0
ansys-mechanical-core                       |       0.10.11
ansys-mechanical-env                        |       0.1.6
ansys-platform-instancemanagement           |       1.1.2
ansys-pythonnet                             |       3.1.0rc6
ansys-tools-common                          |       0.4.3
ansys-tools-path                            |       0.3.2
ansys-workbench-core                        |       0.7.0
debugpy                                     |       1.8.20
numpy                                       |       2.4.2
packaging                                   |       26.0
pandas                                      |       3.0.0
pip                                         |       26.0.1
pywin32                                     |       311
