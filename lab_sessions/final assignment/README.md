# EPA-simmodel

problem_formulation.py: File that defines 5 problem formulations. 
These include the necessary input, the levers, the objectives and the way the input gets translated into outcomes (based on dike_model_functions):
0. 2 objective problem formulation: 
 - damage + investment cost minimaliseren (for dike heightening and rfr together)
 - expected deaths minimaliseren
1. 3 objective problem formulation:
 - investment cost (min) (for dike heightening and rfr together)
 - expected damage cost (min) (for dike heightening and rfr together)
 - expected deaths (min)
2. 5 objective problem formulation:
 - investment specific for room for the river
 - investment specific for dike heightening
 - expected damage
 - expected evacuation cost
 - expected deaths
3. 4 objectives but then split up between locations 
 - investment + annual damage for dikes
 - expected number of deaths
 - total cost for room for the river
 - expected evacuation cost
 
QUESTION: why take annual damage and dike investment together? Arent annual damages also caused by rfr?
4. 
5. 

Problem Formulation.ipynb: 