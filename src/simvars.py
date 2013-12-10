# File:
#     SimVars.py
# Version:
#     0.0.1
# Description:
#     This is the class definition for assorted simulation variables needed for the LIF simulation.
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata
# TODO:
#     - 

# -----------------------------------------------
# Preprocessing:

import numpy as np

from xfddata import XfdData

# -----------------------------------------------
# Class definition:

class SimVars(object):
    def __init__(self, decay_const):

        # How fast each cell's activity should decay,
        #    approximately in activity units per millisecond
        self.decay_const = decay_const
