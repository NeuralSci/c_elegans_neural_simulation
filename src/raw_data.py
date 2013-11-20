# File:
#     raw_data.py
# Version:
#     0.0.1
# Description:
#     This is class definition for the isomorphic representation of the raw data, including methods to read it in from the original CSV file.
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata
# TODO:
#     - 


# -----------------------------------------------
# Preprocessing:

import numpy as np
import pandas as pd

# -----------------------------------------------
# Class definition:

class raw_data(object):
    def __init__(self):
        self.senders, self.receivers, self.types, self.nbrs = [], [], [], []

    def readin_connectome(self):
        """
        This opens the connectome and synapse type CSV files and handles some initial assignments.
        """

        self.varshney_data = pd.read_csv("data/Varshney_et_al/NeuronConnect.csv")

        # Because, alone, a `.iloc` slice of a Pandas dataframe is a Pandas series, which apparently doesn't like indexing as is done in the `data_transformed` class
        self.senders =   np.array(self.varshney_data.iloc[:,0])
        self.receivers = np.array(self.varshney_data.iloc[:,1])
        self.types =     np.array(self.varshney_data.iloc[:,2])
        self.nbrs =      np.array(self.varshney_data.iloc[:,3])

        # original_data.varshney_data.shape[1] = 4

        self.oshio_data = pd.read_csv("data/Oshio_et_al/Ce_synapse/name_neurons_revised.csv", header=None, dtype=str)

        print('Done reading CSV columns to lists. This was way harder than it should have been.')
