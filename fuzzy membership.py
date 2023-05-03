# -*- coding: utf-8 -*-
"""
Created on Wed May  3 23:37:28 2023

@author: Mugen
"""

import numpy as np
import skfuzzy as fuzz

# Define the universe of discourse (input range)
x = np.arange(0, 11, 1)

# Define the fuzzy sets (membership functions)
poor = fuzz.trimf(x, [0, 0, 5])
average = fuzz.trimf(x, [0, 5, 10])
good = fuzz.trimf(x, [5, 10, 10])

# Plot the membership functions
import matplotlib.pyplot as plt
fig, (ax0) = plt.subplots(nrows=1, figsize=(8, 3))

ax0.plot(x, poor, 'b', linewidth=1.5, label='Poor')
ax0.plot(x, average, 'g', linewidth=1.5, label='Average')
ax0.plot(x, good, 'r', linewidth=1.5, label='Good')
ax0.set_title('Membership functions')
ax0.legend()

# Compute the degrees of membership for a given input value
input_value = 4.5
poor_degree = fuzz.interp_membership(x, poor, input_value)
average_degree = fuzz.interp_membership(x, average, input_value)
good_degree = fuzz.interp_membership(x, good, input_value)

print(f'Degree of membership in "poor": {poor_degree:.2f}')
print(f'Degree of membership in "average": {average_degree:.2f}')
print(f'Degree of membership in "good": {good_degree:.2f}')
