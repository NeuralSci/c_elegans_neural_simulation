# File:
#     02_main.py
# Version:
#     0.0.1
# Description:
#     This is the central Python 3 code that will read in the connectome and cell classes, rearrange the connection data, and use that to calculate each neuron's activity as a Leaky-Integrate-and-Fire cell (or, in the future, maybe another type...).
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata
# TODO:
#     - Not fail the class


# -----------------------------------------------
# Preprocessing:

import numpy as np
from raw_data import raw_data
from data_transformed import data_transformed

# -----------------------------------------------
# Connectome read-in and useful rearrangement:

original_data = raw_data()
original_data.readin_connectome()
# Now we've got a nice, workable version of the data to play with.

xform = data_transformed(original_data)
xform.match_cell_class(original_data)
xform.dictionarize_connectome(original_data)
# And now we've got a list of all the individual cells, and dictionaries of them with each cell as a key to a list of cells that connect to that cell.

# # -----------------------------------------------
# # Simulation setup:
# # This will generally follow, for the differential equation,
# #
# #     dx/dt = -A * x + I
# #
# #     Where `x` is the individual neuron's 'activity level', roughly corresponding to its voltage, `A` is the decay constant of the individual cell's activity, I
# #
# #
# 
# 
# # ----------------------
# # Numeric parameters
# 
# time_total = 10 # in milliseconds
# # Eventually:
# # time_total = 1000 # in milliseconds
# dt = 0.01         # in milliseconds
#                   # Note: This level of precision is necessary for proper Hodgkin-Huxley neural model Euler-method integration, and so will be used here just to be safe
# 
# # ----------------------
# # Simulation parameters
# decay_constant = 1
# 
# # ----------------------
# # Initialization
# 
# # The 'state' in the State Variables:
# X_voltage = np.zeros(len(cells))
# # Consider random initial conditions
# 
# # The differential contribution to the state, roughly 'dx' of 'dx/dt', so to speak (if you are a mathematician, I apologize).
# D_voltage = np.zeros(len(cells))
# 
# 
# # ----------------------
# # Integration
# 
# # for ii in range(0.0, time_total, dt):
# #     for index_cell, cell in enumerate(cells):
# #         D_voltage[index_cell] = X_voltage[index_cell] * 2
# 
# #         for index_sender, sender in enumerate(receiver_dict[cell]):
# #             if (type_dict[cell][index_sender] == 'EJ'):
# 
# #             elif ((type_dict[cell][index_sender] == 'S') || (type_dict[cell][index_sender] == 'Sp')):
# 
# #             elif ((type_dict[cell][index_sender] == 'R') || (type_dict[cell][index_sender] == 'Rp')):
# #             D_voltage[index_cell] += 
# 
# 
