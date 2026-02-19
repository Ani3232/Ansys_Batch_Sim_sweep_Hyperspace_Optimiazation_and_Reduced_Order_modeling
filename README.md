

# Ansys Workbench Parameter Sweep and Optimization Automation (Expanded README)

## 📌 Project Overview

This repository provides a **Python-based automation framework** for performing **parameter sweeps** with **ANSYS Workbench** in batch mode. It enables systematic exploration of design variables by programmatically launching and controlling simulation jobs, gathering results, and supporting future integration with optimization and reduced-order workflows.

Parameter sweeps are useful for:

* exploring design sensitivities
* finding optimal parameter combinations
* preparing datasets for surrogate models or reduced-order modeling
* automating massive simulation batches without manual Workbench interaction

This tool works by connecting to a running Ansys Workbench session and controlling simulations via scripting. ([GitHub][1])

---

## 📂 Repository Structure

```
/
├── ansys_files/                # Ansys Workbench project files & templates
├── config/                     # Configuration and template settings
├── dataset/                    # Input/Output data CSVs for sweep results
├── src/                        # Python automation logic
│   ├── ansys_runner.py         # Interface for connecting and running Workbench
│   |── sweep.py                # Control loop for executing parameter sweeps
|   |── clean_logs.py           # Used to clear the stored logs
|   |── dataset_gen.py          # Used to generate dataset for the sweep
|   |── main.py                 # This one combines the total process sequentially
├── .gitignore
└── README.md                   # Project documentation
```

Description of key components:

* **ansys_runner.py** – Handles connection to an active Workbench session and runs simulation jobs.
* **sweep.py** – Manages sweep loops, updates design variable values, launches runs, collects results.
* **dataset/** – Structure for storing generated CSV data (configurable as input and output). ([GitHub][1])

---

## ⚙️ Prerequisites

Before using this automation:

### Software

1. **Ansys Workbench** installed & licensed.
2. Python 3.8+ installed (matching Workbench supported environment).
3. Required Python packages installed (e.g., `pandas`, `pywin32` or other connector libs).

### Workbench Setup

* A parametric Workbench file with named parameters to be swept.
* Ability to start Workbench in server or headless mode that accepts external automation commands.

---

## ▶️ Basic Usage

1. **Launch Ansys Workbench**

   * Open your project or start a session in parametric mode.

2. **Run the Sweep Script**

   ```bash
   python src/sweep.py
   ```

   When prompted, **enter the Workbench server port number** to connect.

3. **Monitor Progress**

   * The script will iterate through your design parameters, execute each simulation, save results to `dataset/`.

4. **Post-Processing**

   * Use the generated `.csv` files for analysis, plotting, or feeding into optimization routines.

---

## 🧠 Typical Workflow

The parameter sweep typically follows this pattern:

1. Initialize connection to Workbench through a COM or socket interface.
2. Read design variable list and ranges.
3. Loop over design points:

   * Update variables in Workbench
   * Trigger new simulation run
   * Collect results (response metrics)
4. Save output data at each step.

This mimics typical parameter sweep utilities in Ansys tools where multiple configurations are explored automatically. ([optics.ansys.com][2])

---

## 🚀 Extensions (Beyond Basic Sweep)

This framework is designed to scale toward advanced tasks:

### 1. **Hyperspace Optimization**

* Replace simple sweeping with directed optimization (e.g., gradient-based, genetic).
* At each iteration, update design variables based on objective evaluations.

### 2. **Reduced-Order Modeling (ROM)**

* Use the sweep dataset to build surrogate models (e.g., POD, regression, Gaussian processes).
* Predict responses without running expensive simulations.

### 3. **Sensitivity & Surrogate Analysis**

* Compute parameter sensitivities from sweep results.
* Visualize parameter influence across design space.

---

## 🛠 Integration Tips

* **Workbench Scripting:** Use Workbench script interface (via Python or IronPython) to programmatically set parameters and run simulations.
* **Data Storage:** Standardize CSV result formats for easier ingestion into optimization or machine learning tools.
* **Parallelization:** Consider launching multiple Workbench instances on separate ports for parallel sweep execution.

---

## 🧩 Example Workflow Snippet

Pseudocode illustrating automation logic:

```
connect_to_workbench(port)
for each design_point in sweep_space:
    set_parameters(design_point.config)
    run_simulation()
    results = fetch_results()
    save_to_csv(results)
```

> Note: Actual implementation depends on Workbench API and runner configuration.

---

## 🧪 Testing & Validation

* Validate connectivity with a small sweep (2–3 points) before launching full batch.
* Cross-verify Workbench results manually in GUI for correctness.
* Check for port availability and server connection timeouts.

---

## 📦 Requirements

Include this in a `requirements.txt` if sharing the project:

```
pandas
numpy
pywin32   # if using Windows COM for Workbench
```

---

## 📄 License & Contributions

* Choose a license (MIT, Apache 2.0 for open-source usage).
* Accept contributions via pull requests.

---

## 📌 Notes

* This repository currently has no stars or forks; consider adding topics and description to attract users. ([GitHub][3])
* Integrate with established parameter sweep tools in Ansys where relevant. ([optics.ansys.com][4])


