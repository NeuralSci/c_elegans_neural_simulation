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

# Libraries
import ipdb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import time

# Custom classes
import rawdata   as rd
import simvars   as smv
import statevars as stv
import timevars  as tiv
import xfddata   as xd

def main(argv = None):
    """
    This is run like with `python src/02_main.py <time in ms> <se weight> <mo weight> <in weight> <spike threshold> <noise magn> <stim magn>`
    """

    # -----------------------------------------------
    # Connectome read-in and useful rearrangement:
    
    start = time.clock()
    
    raw_data = rd.RawData()
    raw_data.readin_connectome("input/Varshney_et_al/NeuronConnect_revised.csv",
                               "input/Oshio_et_al/Ce_synapse/name_neurons_revised.csv")
    # Now we've got a nice, workable version of the data to play with.
    # Note that these files are REVISED from the original data available from the site in the README, in order for coordination between the Varshney (synapse) and Oshio (cell type/class) information to both be used.
    # Specifically, in the Oshio et al. file "name_neurons.txt", which is in plain "Ce_synapse"
    #     1. Commas replaced spaces as the delimiters
    #     2. Lines 29-37, first column, had 0's inserted before single digits to match Varshney names
    #     3. Line 63, first column, the neuron name 'avfr' is now uppercased
    #     4. Lines 89-110, first column, had 0's inserted before single digits to match Varshney names
    #     5. Lines 261-269, first column, had 0's inserted before single digits to match Varshney names
    #     6. Lines 273-281, first column, had 0's inserted before single digits to match Varshney names
    #     7. Lines 284-298, first column, had 0's inserted before single digits to match Varshney names
    #     8. Lines 62-64, 71, 112, 126-131, 143-144, 149, 177-179, 184, 194, 206-213, 218-223, 241-256, third column, cells with ambiguous cell class information had their first value used solely, since we are assuming it is more likely or more prevalent.
    #
    # In the Varshney et al. file "NeuronConnect.xls",
    #     1. Line 1872, first and second columns, uppercased 'avfr'
    #     2. Lines 6266-6418, removed 'NMJ' receiving neuron data, since at the moment we don't care about muscle firing, but mostly that the NMJs are not distinguished here.

    sensoryneuron_weight = argv[2]
    motorneuron_weight =   argv[3]
    interneuron_weight =   argv[4]
    thresh =               float(argv[5])
    noise_magnitude =      float(argv[6])
    stim_magnitude =       float(argv[7])

    xfd_data = xd.XfdData()
    xfd_data.match_cell_class(raw_data)
    xfd_data.assign_weights(raw_data, sensoryneuron_weight, motorneuron_weight, interneuron_weight)
    xfd_data.dictionarize_connectome(raw_data)
    # And now we've got a list of all the individual cells, and dictionaries of them with each cell as a key to a list of cells that connect to that cell.

    time_readin = time.clock() - start
    print("Time taken for data readin and arrangement:", time_readin, "seconds")

    # ----------------------
    # Numeric parameters

    # Note: This level of precision is necessary for proper Hodgkin-Huxley neural model Euler-method integration, and so will be used here just to be safe
    time_vars = tiv.TimeVars(        dt =    0.01,   # in milliseconds
                             time_total =    float(argv[1])  )  # in milliseconds


    # ----------------------
    # Simulation parameters
    # - Apparently, must pass in variable defn of the same name as the attribute, oddly enough...
    sim_vars = smv.SimVars(decay_const = 1)

    # ----------------------
    # Integration

    state_vars = stv.StateVars(xfd_data)

    state_vars.integrate(xfd_data, sim_vars, time_vars, thresh, noise_magnitude, stim_magnitude)

    time_integration = time.clock() - time_readin

    print("Time taken for simulation of", time_vars.time_total, "ms :", time_integration, "seconds")

    # ----------------------
    # Plotting

    final_data = pd.read_csv('output/activity_output.csv')

    activity_plot = plt.figure()
    ax =  activity_plot.add_subplot(111)
    plt.hold('True')
    for neuron in range(1, final_data.shape[1]):
        ax.plot(final_data.iloc[:,0], final_data.iloc[:,neuron], color="k")

    activity_plot.savefig("output/" + "time" + str(time_vars.time_total) \
        + "se" + ("%.3f" % float(sensoryneuron_weight)) \
        + "mo" + ("%.3f" % float(motorneuron_weight)) \
        + "in" + ("%.3f" % float(interneuron_weight)) \
        + "noise" + ("%.3f" % noise_magnitude) \
        + "stim" + ("%.3f" % stim_magnitude) \
        + "total_activity.png", dpi_set=300)


    time_plotting = time.clock() - time_integration
    print("Time taken for plotting", time_plotting, "seconds")

    # ipdb.set_trace()


if (__name__ == "__main__"):
    main(sys.argv)
