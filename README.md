# Network analysis and neural simulation of a C. Elegans connectome
===========================

- This is a final project for MA 703, "Statistical Analysis of Network Data", taught Fall 2013 at Boston University.

- The connectome specifically being used is taken from the [freely available data here](http://www.wormatlas.org/neuronalwiring.html#NeuronalconnectivityII) whose best citation is *Varshney, Chen, Paniaqua, Hall and Chklovskii in "Structural properties of the C. elegans neuronal network" PLoS Comput. Biol. Feb 3, 2011 3:7:e1001066 (doi:10.1371/journal.pcbi.1001066)[http://dx.doi.org/doi:10.1371/journal.pcbi.1001066]*

- The overall goals are to
    1. Use network statistics to characterize triad, etc. motifs present in a directed graph of the connectome that includes the type of synaptic connections,
    2. Paying particular attention to those motifs and other characteristics, look for interesting, and possibly consistent, patterns of behavior by tthe cells involved in these motifs and organizations.

- The minimum requirements are:
    - (The R language)[http://www.r-project.org/], a version recent enough to support...
    - The (igraph)[http://igraph.sourceforge.net/] library for R (it also has a Python interface)


- A rough outline of the software flow (you may get a flowchart soon if you're lucky) is
    1. (Completed) Read in the CSV data into a *igraph* graph object, with all the vertex and edge attribute goodness.
    2. (Not completed) Create and test a probably-Python-based implementation of (Leaky Integrate-and-fire) neurons that can read edge information from either the graph object or the original CSV data.
    3. (Not completed) Research both theoretical capabilities and *igraph* capabilities for finding motifs etc. in the network. Note that the different edge attributes may interfere.
    4. (Not completed) Locate a set of small motifs, run the simulation, and plot the motifs' behavior alongside many non-motif neurons' activity. Look for anything interesting.
    5. (Not completed) Do spectral analysis on the neurons if their behavior is rhythmic at all, or even if not.
    6. Repeat 4 and 5 with either different motifs, or differently sized ones, or another statistic (?) altogether.

