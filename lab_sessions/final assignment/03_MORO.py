import pandas as pd
from problem_formulation import get_model_for_problem_formulation
from ema_workbench.analysis import plotting, plotting_util, pairs_plotting, prim
from ema_workbench import (RealParameter, ScalarOutcome, Constant,
                           Model, MultiprocessingEvaluator, SequentialEvaluator, ema_logging,
                           perform_experiments, Policy, Scenario)
from ema_workbench.em_framework.salib_samplers import get_SALib_problem
from ema_workbench.em_framework.samplers import sample_uncertainties
from ema_workbench.em_framework.optimization import (HyperVolume,
                                                     EpsilonProgress)
from ema_workbench import Constraint
from ema_workbench.util.utilities import (save_results, load_results)
import seaborn as sns
import matplotlib.pyplot as plt

# define problem formulation
model, functions = get_model_for_problem_formulation(2)

# set up robust functions
import functools
import numpy as np


def robustness(direction, threshold, data):
    if direction == 'SMALLER':
        return np.sum(data<=threshold)/data.shape[0]
    else:
        return np.sum(data>=threshold)/data.shape[0]

Expected_Annual_Damage = functools.partial(robustness, 'SMALLER', 1*10**6)
Dike_Investment_Costs = functools.partial(robustness, 'SMALLER', 10*10**8)	
RfR_Investment_Costs = functools.partial(robustness, 'SMALLER', 1)	
Evacuation_Costs = functools.partial(robustness, 'SMALLER', 50000)	
Expected_Number_of_Deaths = functools.partial(robustness, 'SMALLER', 0.5)
Minimum_water_level_full_network = functools.partial(robustness, 'LARGER', 4.5)

# Defining the robustness functions
robust = [ScalarOutcome('Expected_Damage', kind=ScalarOutcome.MAXIMIZE, variable_name='Expected Annual Damage',
                        function=Expected_Annual_Damage),
          ScalarOutcome('Dike_Costs', kind=ScalarOutcome.MAXIMIZE,variable_name='Dike Investment Costs',
                        function=Dike_Investment_Costs),
          ScalarOutcome('RfR_Costs', kind=ScalarOutcome.MAXIMIZE, variable_name='RfR Investment Costs', 
                        function=RfR_Investment_Costs),
          ScalarOutcome('Evacuation_Costs', kind=ScalarOutcome.MAXIMIZE, variable_name='Evacuation Costs',
                        function=Evacuation_Costs),
          ScalarOutcome('Number_of_Deaths', kind=ScalarOutcome.MAXIMIZE, variable_name='Expected Number of Deaths',
                        function=Expected_Number_of_Deaths),
          ScalarOutcome('wl', kind=ScalarOutcome.MAXIMIZE, variable_name='Minimum water level full network',
                        function=Minimum_water_level_full_network)   
          ]


# set up convergence metrics
convergence_metrics = [HyperVolume(minimum=[0,0,0,0,0,0], maximum=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1]), EpsilonProgress()]

# load scenarios from PRIM analysis
import pickle

with open('ANALYSIS_results/02_PRIM_scenarios.txt', 'rb') as file:
    scenarios = pickle.load(file)
    
# perform MORO
ema_logging.log_to_stderr(ema_logging.INFO)

with MultiprocessingEvaluator(model) as evaluator:
    robust_results, convergence = evaluator.robust_optimize(robust, 
                                                    scenarios=scenarios,
                                                    nfe = 101,
                                                    epsilons=[0.05, ] * len(robust),
                                                    convergence=convergence_metrics)
    
# save results
robust_results.to_csv('03_MORO_results.csv')
convergence.to_csv('03_MORO_convergence.csv')