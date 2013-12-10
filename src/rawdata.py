# File:
#     RawData.py
# Version:
#     0.0.2
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

class RawData(object):
    def __init__(self):
        self.senders = []
        self.receivers = []
        self.types = []
        self.nbrs = []

    def readin_connectome(self, file_1, file_2):
        """
        This opens the connectome and synapse type CSV files and handles some initial assignments.
        """

        self.varshney_data = pd.read_csv(file_1)

        # Because, alone, a `.iloc` slice of a Pandas dataframe is a Pandas series, which apparently doesn't like iterating through indexing as is done in the `data_transformed` class
        self.senders = np.array(self.varshney_data.iloc[:,0])
        self.receivers = np.array(self.varshney_data.iloc[:,1])
        self.types = np.array(self.varshney_data.iloc[:,2])
        self.nbrs = np.array(self.varshney_data.iloc[:,3])

        self.oshio_data = pd.read_csv(file_2, header=None, dtype=str)

        print('Done reading CSV columns to lists. This was way harder than it should have been.')
