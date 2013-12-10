# Network analysis and neural simulation of a C. Elegans connectome
===========================

- This is a final project for MA 703, "Statistical Analysis of Network Data", taught Fall 2013 at Boston University.

- The *C. Elegans* connectome specifically being used is taken from the [freely available data here](http://www.wormatlas.org/neuronalwiring.html#NeuronalconnectivityII) whose best citation is 
    - *Varshney, Chen, Paniaqua, Hall and Chklovskii in "Structural properties of the C. elegans neuronal network" PLoS Comput. Biol. Feb 3, 2011 3:7:e1001066 [doi:10.1371/journal.pcbi.1001066](http://dx.doi.org/doi:10.1371/journal.pcbi.1001066)*. 

- Additionally, the cell class (motor, sensory, or interneuron) information was taken from [the open data here](http://www.wormatlas.org/neuronalwiring.html#NeuronalconnecitivityIII) whose citations are
    - *Albertson, D. G. and Thomson, J. N. (1976). "The Pharynx of Caenorhabditis elegans", Phil. Trans. R. Soc. London B 275, pp.229-325.*,   
    - *White, J. G., Southgate, E., Thomson, J. N. and Brenner, S. (1986). "The structure of the nervous system of the nematode Caenorhabditis elegans", Phil. Trans. R. Soc. London B 314, pp.1-340.*, and
    - *Oshio, K., Iwasaki, Y., Morita, S., Osana, Y., Gomi, S., Akiyama, E., Omata, K., Oka, K. and Kawamura, K. (2003). "Database of Synaptic Connectivity of C. elegans for Computation", Technical Report of CCeP, Keio Future, No.3, Keio University.*.

- The overall goals are to
    1. Use network statistics to characterize triad, etc. motifs present in a directed graph of the connectome that includes the type of synaptic connections,
    2. Paying particular attention to those motifs and other characteristics, look for interesting, and possibly consistent, patterns of behavior by tthe cells involved in these motifs and organizations.

- The minimum requirements are:
    - [The R language](http://www.r-project.org/), a version recent enough to support...
    - The [igraph](http://igraph.sourceforge.net/) library for R (it also has a Python interface)
    - [Python 3](http://www.python.org/), although it will probably be trivial to make it Python 2 capable.
    - The [matplotlib](http://matplotlib.org/) plotting library for Python.
    - The [Pandas](http://pandas.pydata.org/) data analysis library for Python.


### A rough outline of the software flow (you may get a flowchart soon if you're lucky) is: ###

1. (Completed) Read in the CSV data into a *igraph* graph object, with all the vertex and edge attribute goodness.
2. (Not completed) Create and test a Python implementation of (Leaky Integrate-and-fire) neurons that can read edge information from either the graph object or the original CSV data.
    1. (Completed) Read in the CSV data into manageable Python structures.
    2. (Completed) Rearrange the data into more manageable data structures that contain directional synapse information, cell class information, and minimal/no redundancy. I ended up using Pandas to put them into dictionaries and Numpy arrays. This was way harder to learn than expected, but is now shown to be very simple.

3. (Not completed) Research both theoretical capabilities and *igraph* capabilities for finding motifs etc. in the network. Note that the different edge attributes may interfere.
4. (Not completed) Locate a set of small motifs, run the simulation, and plot the motifs' behavior alongside many non-motif neurons' activity. Look for anything interesting.
5. (Not completed) Do spectral analysis on the neurons if their behavior is rhythmic at all, or even if not.
6. Repeat 4 and 5 with either different motifs, or differently sized ones, or another statistic (?) altogether.

