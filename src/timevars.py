# File:
#     TimeVars.py
# Version:
#     0.0.1
# Description:
#     This is the class definition for the time variables needed for the LIF simulation.
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata
# TODO:
#     - 

# -----------------------------------------------
# Class definition:

class TimeVars(object):
    def __init__(self, dt, time_total):
        # All attributes of this are in milliseconds.

        # The resolution.
        self.dt = dt
        # The full time to run the simulation for.
        self.time_total = time_total
        # The initial time.
        self.t0 = 0.
        # The actual time, which will increase.
        self.t = 0.


