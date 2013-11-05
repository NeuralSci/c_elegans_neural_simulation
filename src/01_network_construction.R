# File:
#     01_network_construction.R
# Version:
#     0.0.1
# Description:
#     This initial R code will read in the connectome data stored in the `data/` directory and tranform it into an igraph object. This object will also be the source of the synaptic connections to be used in the neural simulation later on.
# Project:
#     Z004: Network analysis and neural simulation of the C. Elegans connectome, MA 703, Fall 2013, Final Project, Austin Soplata

# Preprocessing:
library(igraph)

# -----------------------------------------------
### Notes on NeuronData.csv ###
# - Many of the cells that connect to NMJ's, like where the '2nd neuron' is NMJ, are cells with valid synapses to/fro elsewhere.

raw <- read.csv("data/NeuronConnect.csv")

cxn <- read.graph("celegansneural/celegansneural.gml", format = c("gml"))


# -----------------------------------------------
### Problem 4.1, part B ###

# # sample plot:
# png('fig02_part_4_2a.png')
# par(mfrow = c(1,2))
# plot(hw_g_4.2a)
# dev.off() # don't forget!



alpha_1 <- 3
alpha_2 <- 10
x_lowest_1 <- 2
x_lowest_2 <- 10
n_pareto_1 <- 20
n_pareto_2 <- 200

# Because no one ever agrees on terminology ever, 
#    the authors' code translates via:
#
#    their k     = our alpha
#    their alpha = our x_0
#
# for use in `rpareto(n_samples, their alpha, their k)`

sample_pareto_1 <- rpareto(n_pareto_1, x_lowest_1, alpha_1)
sample_pareto_2 <- rpareto(n_pareto_2, x_lowest_2, alpha_2)

Hill_estimation <- function(samples, lowest_value) {
    # Initialize.
    estimator <- 0

    for (ii in 1:length(samples)){
        estimator = estimator + log(samples[ii] / lowest_value)
    }
    estimator = (1 / length(samples)) * estimator
    estimator = 1 / estimator
    return(estimator)
}

Hill_1 <- Hill_estimation(sample_pareto_1, x_lowest_1)
Hill_2 <- Hill_estimation(sample_pareto_2, x_lowest_2)

#### Now to compare to naive regression, equation 4.2
y_1 <- log(dpareto(seq(from = x_lowest_1 + 0.0001, to = n_pareto_1,
                       by = (n_pareto_1 - x_lowest_1 + 0.0001)/n_pareto_1),
                   x_lowest_1,
                   alpha_1))
x_1 <- -log(sample_pareto_1)
frame_1 <- data.frame(y_1, x_1)
fit_1 <- lm(y_1 ~ x_1, frame_1)

y_2 <- log(dpareto(seq(from = x_lowest_2 + 0.0001, to = n_pareto_2, 
                           by = (n_pareto_2 - x_lowest_2 + 0.0001)/n_pareto_2),
                   x_lowest_2,
                   alpha_2))
x_2 <- log(sample_pareto_2)
frame_2 <- data.frame(y_2, x_2)
fit_2 <- lm(y_2 ~ x_2, frame_2)

#### Now to compare to equation 4.3
# to see if changing the probability's alpha to see if it's guiding the regression
y_probs_1 <- log(1 - ppareto(sample_pareto_1, x_lowest_1, alpha_1 + 1))
x_probs_1 <- -log(sample_pareto_1)
frame_probs_1 <- data.frame(y_probs_1, x_probs_1)
fit_probs_1 <- lm(y_probs_1 ~ x_probs_1, frame_probs_1)

y_probs_2 <- log(1 - ppareto(sample_pareto_2, x_lowest_2, alpha_2))
x_probs_2 <- -log(sample_pareto_2)
frame_probs_2 <- data.frame(y_probs_2, x_probs_2)
fit_probs_2 <- lm(y_probs_2 ~ x_probs_2, frame_probs_2)


# -----------------------------------------------
### Problem 4.2 ###

hw_g_4.2a <- graph.formula(1-S, S-3, 3-V, V-Z, Z-6, 6-T)
V(hw_g_4.2a)["S"]$color <- "blue"
V(hw_g_4.2a)["V"]$color <- "green"
V(hw_g_4.2a)["Z"]$color <- "orange"
V(hw_g_4.2a)["T"]$color <- "red"

# png('fig02_part_4_2a.png')
# plot(hw_g_4.2a)
# dev.off() # don't forget!

hw_g_4.2b <- graph.formula(S-2, S-7, 2-V, 7-altV, V-Z, altV-Z, Z-5, Z-8, 8-T, 5-T)
V(hw_g_4.2b)["S"]$color <- "blue"
V(hw_g_4.2b)["V"]$color <- "green"
V(hw_g_4.2b)["altV"]$color <- "green"
V(hw_g_4.2b)["Z"]$color <- "orange"
V(hw_g_4.2b)["T"]$color <- "red"

# png('fig03_part_4_2b.png')
# plot(hw_g_4.2b)
# dev.off() # don't forget!

# -----------------------------------------------
### Problem 4.3 ###
hw_g1_4.3a <- graph.formula(1-2, 2-3, 3-1)
hw_g2_4.3a <- graph.formula(1-2, 2-3)

# png('fig04_part_4_3a.png')
# par(mfrow = c(1,2))
# plot(hw_g1_4.3a)
# plot(hw_g2_4.3a)
# dev.off() # don't forget!


hw_g1_4.3b <- graph.formula(1-2, 1-3,
                            2-3,
                            4-2, 4-3,
                            5-2, 5-3)

# png('fig05_part_4_3b.png')
# plot(hw_g1_4.3b)
# dev.off() # don't forget!


# -----------------------------------------------
### Problem 4.4 ###

hw_g1_4.4a <- graph.formula(2-4, 2-5, 2-6, 2-7, 6-7,
                            3-8, 3-9, 3-10, 3-11, 8-9, 8-11, 10-11)

# png('fig06_part_4_4a.png')
# plot(hw_g1_4.4a)
# dev.off() # don't forget!

big_L <- graph.laplacian(hw_g1_4.4a)

degen_egval_1 <- c(1, 1, 1, 1, 1,
                   0, 0, 0, 0, 0)

degen_egval_2 <- c(0, 0, 0, 0, 0,
                   1, 1, 1, 1, 1)

egdecomp <- eigen(big_L)

hw_g1_4.4b <- graph.formula(2-4, 2-5, 2-6, 2-7, 6-7,
                            3-8, 3-9, 3-10, 3-11, 8-9, 8-11, 10-11,
                            2-3)

big_L1_4.4b <- graph.laplacian(hw_g1_4.4b)
egdecomp_1_4.4b <- eigen(big_L1_4.4b)

hw_g2_4.4b <- graph.formula(2-4, 2-5, 2-6, 2-7, 6-7,
                            3-8, 3-9, 3-10, 3-11, 8-9, 8-11, 10-11,
                            2-3, 9-7, 8-6, 5-3, 4-11)

big_L2_4.4b <- graph.laplacian(hw_g2_4.4b)
egdecomp_2_4.4b <- eigen(big_L2_4.4b)

# png('fig07_part_4_4b.png')
# plot(hw_g2_4.4b)
# dev.off() # don't forget!



# -----------------------------------------------
### Problem 4.5 ###

cxn <- read.graph("celegansneural/celegansneural.gml", format = c("gml"))

dgr <- degree(cxn)

# png('fig08_part_4_5.png')
# plot(density(dgr), main="Probability density of the C. Elegans degree sequence")
# dev.off() # don't forget!


V(cxn)[degree(cxn) > 50]$color <- "red"
# V(cxn)[degree(cxn) > 50]$size <- 3*sqrt(graph.strength(cxn)

# png('fig09_part_4_5.png')
# # par(mfrow = c(2,2))
# # plot(cxn, layout = layout.auto)
# # plot(cxn, layout = layout.sphere)
# plot(cxn, layout = layout.kamada.kawai)
# # plot(cxn, layout = layout.spring)
# 
# # plot(cxn, vertex.size = v.size, edge.width = e.wgts, layout = layout.fruchterman.reingold)
# dev.off() # don't forget!

# png('fig10_part_4_5.png')
# par(mfrow = c(2,1))
# plot(betweenness(cxn), main="Vertex Betweenness")
# plot(transitivity(cxn, type=c("local")), main="Transitivity")
# dev.off() # don't forget!

# png('fig11_part_4_5.png')
# plot(edge.betweenness(cxn), main="Edge Betweenness")
# dev.off() # don't forget!

E(cxn)[edge.betweenness(cxn) > 1000]$color <- "green"

# png('fig12_part_4_5.png')
# plot(cxn, layout = layout.kamada.kawai)
# dev.off() # don't forget!


v.size <- sqrt(sqrt((betweenness(cxn))))
# V(cxn)[betweenness(cxn) > 2000]$shape <- "square"

# png('fig13_part_4_5.png')
# plot(cxn, layout = layout.kamada.kawai, vertex.size = v.size)
# dev.off() # don't forget!
