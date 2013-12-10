# File:
#     XfdData.py
# Version:
#     0.0.2
# Description:
#     This is the class definition for the transformed & rearranged data, that will make it significanly easier to use in a neural network model that uses its synapse information.
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata
# TODO:
#     - 


# -----------------------------------------------
# Preprocessing:

import ipdb
import numpy as np

from rawdata import RawData

# -----------------------------------------------
# Class definition:

class XfdData(object):
    def __init__(self):
        self.receiver_dict = {}

        self.receiver_index_list = []
        self.receiver_number_list = []

        self.type_dict = {}
        self.nbr_dict = {}
        self.class_dict = {}
        # If there was a way to make these dicts `const` or immutable somehow after `dictionarize_connectome()`, that would be nice


    def assign_weights(self, RawData, se_wgt, mo_wgt, in_wgt):
        for cell_index, cell_value in enumerate(self.cells):
            for oshio_index, oshio_value in enumerate(RawData.oshio_data[0]):
                if (oshio_value == cell_value):
                    # There are a lot of assumptions going on here...
                    # If one wanted draws from a distribution, or a class-specific distribution, this would be the place.
                    if (RawData.oshio_data[2][oshio_index] == 'se'):
                        self.class_weights[cell_index] = se_wgt
                    elif (RawData.oshio_data[2][oshio_index] == 'mo'):
                        self.class_weights[cell_index] = mo_wgt
                    elif (RawData.oshio_data[2][oshio_index] == 'in'):
                        self.class_weights[cell_index] = in_wgt


    def dictionarize_connectome(self, RawData):
        """
        Determine dicts whose keys are cell names, and whose values are LISTS of cell names, synapse types, and synapse numbers that send to that keyed cell name.
        """

        sender_list = []
        type_list = []
        nbr_list = []

        for target_index, target in enumerate(self.cells):
            for index, source in enumerate(RawData.senders):
                # This is apparently EXACTLY how you're supposed to used enumerate()
                if (RawData.receivers[index] == str(target)):
                    sender_list.append(str(source))
                    type_list.append(str(RawData.types[index]))
                    nbr_list.append(RawData.nbrs[index])

            self.receiver_dict[str(target)] = sender_list

            sender_index_list = []

            for sender in sender_list:
                sender_index_list.append(np.where(self.cells == sender)[0][0])

            self.receiver_index_list.append(sender_index_list)
            self.receiver_number_list.append(nbr_list)

            self.type_dict[str(target)] = type_list
            self.nbr_dict[str(target)] = nbr_list

            sender_list = []
            type_list = []
            nbr_list = []



    def match_cell_class(self, RawData):
        """
        Determine `cells` and `class_dict` attributes.
        """

        self.cells = np.unique(RawData.receivers)
        self.class_weights = np.zeros(len(self.cells))

        # Create a dict whose keys are cell name strings and whose values are that cell's cell class; also create a list, arranged like `self.cells`, with outgoing synaptic weights that correspond to its cell class.
        for cell_index, cell_value in enumerate(self.cells):
            for oshio_index, oshio_value in enumerate(RawData.oshio_data[0]):
                if (oshio_value == cell_value):
                    self.class_dict[cell_value] = RawData.oshio_data[2][oshio_index]
