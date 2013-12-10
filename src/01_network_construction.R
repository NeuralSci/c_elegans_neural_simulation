# File:
#     01_network_construction.R
# Version:
#     0.0.1
# Description:
#     This initial R code will read in the connectome data stored in the `data/` directory and tranform it into an igraph object. This object will also be the source of the synaptic connections to be used in the neural simulation later on.
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata
# TODO:
#     - All the actual network statistics

# -----------------------------------------------
# Preprocessing:
library(igraph)
library(ggplot2)

# -----------------------------------------------

raw <- read.csv("input/Varshney_et_al/NeuronConnect_revised.csv")
# Seems to do the job, surprisingly
cxn <- graph.data.frame(raw)

V(cxn)

# cxn <- read.graph("celegansneural/celegansneural.gml", format = c("gml"))

activ <- read.csv("output/activity_output.csv")
cells <- attributes(activ)$names

png("output/fig01_total_activity.png")
ts.plot(activ[,2:280])
dev.off()


