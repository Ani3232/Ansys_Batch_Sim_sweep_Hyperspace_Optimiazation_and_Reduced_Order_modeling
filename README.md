# Ansys Workbench Parameter Sweep

This project automates parameter sweeps in Ansys Workbench.

## Folder Structure
- `/src` - Python scripts
  - `ansys_runner.py` - Main solver interface
  - `sweep.py` - Parameter sweep controller
- `/dataset` - Input/output CSV files

## Usage
1. Start Ansys Workbench server
2. Run `python src/sweep.py`
3. Enter port number when prompted