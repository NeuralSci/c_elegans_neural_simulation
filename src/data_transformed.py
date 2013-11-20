# File:
#     data_transformed.py
# Version:
#     0.0.1
# Description:
#     This is the class definition for the transformed & rearranged data, that will make it significanly easier to use in a neural network model that uses its synapse information.
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata
# TODO:
#     - 


# -----------------------------------------------
# Preprocessing:

import numpy as np
from raw_data import raw_data

# -----------------------------------------------
# Class definition:

class data_transformed(raw_data):
    def __init__(self, raw_data):
        self.receiver_dict, self.type_dict, self.nbr_dict, self.class_dict = {}, {}, {}, {}


    def match_cell_class(self, raw_data):
        """
        Determine `cells` and `class_dict` attributes.
        """

        self.cells = np.unique(raw_data.receivers)

        # TODO: make a note of the data changes that had to happen
            # - both the 0's added to Oshio, and NMJ and avfr
            # capitalize avfr, and delete NMJ in Varshney?

        for cell_index, cell_value in enumerate(self.cells):
            for oshio_index, oshio_value in enumerate(raw_data.oshio_data[0]):
                if (oshio_value == cell_value):
                    self.class_dict[cell_value] = raw_data.oshio_data[2][oshio_index]



    def dictionarize_connectome(self, raw_data):
        """
        Determine dicts whose keys are cell names, and whose values are LISTS of cell names, synapse types, and synapse numbers that send to that keyed cell name.
        """

        sender_list = []
        type_list = []
        nbr_list = []

        for target in self.cells:
            # This is apparently EXACTLY how you're supposed to used enumerate()
            for index, source in enumerate(raw_data.senders):
                if (raw_data.receivers[index] == str(target)):
                    sender_list.append(str(source))
                    type_list.append(str(raw_data.types[index]))
                    nbr_list.append(str(raw_data.nbrs[index]))

            self.receiver_dict[str(target)] = sender_list
            self.type_dict[str(target)] = type_list
            self.nbr_dict[str(target)] = nbr_list

            sender_list = []
            type_list = []
            nbr_list = []
