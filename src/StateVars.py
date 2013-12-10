# File:
#     StateVars.py
# Version:
#     0.0.1
# Description:
# 
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata
# TODO:
#     - 

# -----------------------------------------------
# Preprocessing:

import csv
import ipdb
import numpy as np
import pickle
import time

from xfddata  import XfdData
from simvars  import SimVars
from timevars import TimeVars

# -----------------------------------------------
# Class definition:

class StateVars(object):
    def __init__(self, XfdData):
        # The 'state' in the State Variables:
        np.random.seed()
        self.x_activity = np.random.rand(len(XfdData.cells))
        # self.x_activity = np.zeros(len(XfdData.cells))

        # The differential contribution to the state, roughly 'dx' of 'dx/dt', so to speak (if you are a mathematician, I apologize).
        self.dxdt_activity = np.zeros(len(XfdData.cells))


    def integrate(self, XfdData, SimVars, TimeVars, spike_threshold, noise_strength, stim_strength):
        """
        Solve the system. Also describe this method a tad more.
        """

        # -----------------------------------------------
        # Simulation setup:
        # This will generally follow, for the differential equation,
        #
        #     dx/dt = -A * x + I
        #
        #     Where `x` is the individual neuron's 'activity level', roughly corresponding to its voltage, `A` is the decay constant of the individual cell's activity, I
        #

        with open('output/activity_output.csv', 'w', newline='') as csvfile:
            counter = 0

            # First, write the headers to the output data.
            csvfile.write("Time")
            for ii in range(0,len(self.x_activity)):
                csvfile.write("," + XfdData.cells[ii])

            csvfile.write("\n")

            while (TimeVars.t < TimeVars.time_total):

                ### "This is where the magic happens."
                # I WOULD put this in its own function that's called a million
                #    times, but
                #    1. calls are supposed to be relatively expensive in Python
                #    2. It's simple enough that it's just a few lines.
                for index_cell, cell in enumerate(XfdData.cells):
                    self.dxdt_activity[index_cell] = - SimVars.decay_const * self.x_activity[index_cell]

                    for index_in_receiver_list, index_sender in enumerate(XfdData.receiver_index_list[index_cell]):
                        self.dxdt_activity[index_cell] += XfdData.receiver_number_list[index_cell][index_in_receiver_list] \
                            * XfdData.class_weights[index_sender] * self.x_activity[index_sender]
                        # self.dxdt_activity[index_cell] += XfdData.class_weights[index_sender] * self.x_activity[index_sender]

                    self.x_activity[index_cell] += TimeVars.dt * self.dxdt_activity[index_cell] + (noise_strength*np.random.randn(1))[0] + stim_strength
                    # self.x_activity[index_cell] += TimeVars.dt * self.dxdt_activity[index_cell]

                    if (self.x_activity[index_cell] > spike_threshold):
                        self.x_activity[index_cell] = -1.





                ### Then, write this just-calculated iteration to file.
                csvfile.write(str(("%.2f" % TimeVars.t)))
                for ii in range(0,len(self.x_activity)):
                    csvfile.write("," + str(str(self.x_activity[ii])))

                csvfile.write("\n")

                ### Then, if a certain point is reached, tell the user so they don't
                # stare at the screen for five minutes.
                # Apparently, instead supposed to use an epsilon for this logical check.
                if (((float("%.2f" % TimeVars.t) % (float("%.2f" % TimeVars.time_total) * 0.25)) == 0.) and (counter == 0) and (float("%.2f" % TimeVars.t) != 0.0)):
                    print("Simulation 25% complete.")
                    counter += 1
                elif (((float("%.2f" % TimeVars.t) % (float("%.2f" % TimeVars.time_total) * 0.25)) == 0.) and (counter == 1)):
                    print("Simulation 50% complete.")
                    counter += 1
                elif (((float("%.2f" % TimeVars.t) % (float("%.2f" % TimeVars.time_total) * 0.25)) == 0.) and (counter == 2)):
                    print("Simulation 75% complete.")
                    counter += 1

                TimeVars.t += TimeVars.dt
