import numpy as np
from scipy.optimize import fsolve

def f(x):
    return 19 * np.exp(x) * np.cos(x) - 9 * np.exp(np.sin(x)) - 7 * np.log(x+1) + 7

# finding the first positive root
initial_guess = 1
root = fsolve(f, initial_guess)

print(f'First Positive Root: {root[0]}')
