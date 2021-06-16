# EPA-simmodel

The room for the river project model is included. For the analysis steps 6 jupyter notebooks have been used

ANALYSIS_00_problem_formulations.ipynb
ANALYSIS_01_scenario_discoveryipynb
ANALYSIS_02_PRIM.ipynb
ANAlYSIS_03_MORO.ipynb
ANALYSIS_04_SOBOL.ipynb
ANALYSIS_05_robustness.ipynb

## outputs
(intermediate) Results are stored in the folder ANALYSIS_results with corresponding labels to the notebook they have been generated in.


## adjustments to the model
For the analysis the original room for the river model (https://github.com/quaquel/epa1361_open) has been used with a single adjustment.
The problem_formulation.py file now includes minimal water level output for the second problem formulation which is the problem formulation used in this analysis. 

problem_formulation.py: File that defines 5 problem formulations. 
These include the necessary input, the levers, the objectives and the way the input gets translated into outcomes (based on dike_model_functions):
Problem formulation 2. 6 objective problem formulation:
 - investment specific for room for the river
 - investment specific for dike heightening
 - expected damage
 - expected evacuation cost
 - expected deaths
 - Minimal Water Level


## ANALYSIS_00_problem_formulations.ipynb

Inspect the problem formulations and check if the minimal water level has been correctly reported.

Inputs: problem formulation
Outputs: none


## ANALYSIS_01_scenario_discovery.ipynb

Scenario discovery for 100 random policies and 500 random scenarios with LHS sampling

Input: Problem formulation
Output: ANALYSIS_results/01_model_run.tar.gz (result of 100 policy, 500 scenario run)


## ANALYSIS_02_PRIM.ipynb

Run PRIM analysis on the scenario discovery to determine the worst case scenarios

Input: ANALYSIS_results/01_model_run.tar.gz
Output: ANALYSIS_results/02_PRIM_scenarios.txt (worst case scenarios according to PRIM analysis)

## ANAlYSIS_03_MORO.ipynb

Run MORO analysis with 100 randomly sampled scenarios 10000 nfe and epsilon values of 0.05. 
Re-run experiments with the found policies and 10 random policies. 

Input: none
Outputs: 
ANALYSIS_results/03_MORO_results.csv (MORO policy outcomes)
ANALYSIS_results/03_MORO_convergence.csv (MORO convergence information)
ANALYSIS_results/03_robust_results.tar.gz (Results of re-run with found and random policies.)


## ANALYSIS_04_SOBOL.ipynb

Sobol analysis for the found solutions with 1200 scenarios

input: ANALYSIS_results/03_MORO_results.csv
Output: ANALYSIS_results/04_sobol_results.tar.gz

## ANALYSIS_05_robustness.ipynb

Run robustness analysis

input:
output:



