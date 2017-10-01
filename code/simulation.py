"""
Performs the susceptible-infected-susceptible simulation of spread of
viruses/disease through connected networks

Wrtie Down each individual steps very clearly before any implementation

1. generate a network
2. generate some percentage of initially infected nodes
3. for some # of time steps, run simulation of concurrent infection/recovery

"""

import random
import numpy as np


def flip(p):
    return np.random.random() < p


def run_SIS_simulation(graph, lam, rho_0=0.5, time_steps=1000):
    """
    Arguments:
    graph : a networkx graph
    lam : lambda, the spreading rate which is a ratio v / d where v is the
            infection rate and d is the recovery rate. We fix d = 1 without
            loss of generality.
    rho_0 : the initial infection fraction

    Returns:
    final infection fraction rho
    """
    infected_nums = np.zeros(time_steps)
    # initial state
    infected = set(random.sample(graph.nodes(), int(graph.number_of_nodes() * rho_0)))
    # begin time steps
    for t in range(time_steps):
        infected_nums[t] = len(infected) / float(graph.number_of_nodes())
        # susceptible nodes that are adjacent to infected nodes
        at_risk = set()
        for inf in infected:
            at_risk.update(set(graph[inf]))
        # remove any currently infected nodes from at_risk
        at_risk.difference_update(infected)
        # infected nodes are cured with a probability of d = 1
        infected = set()
        # roll for at_risk nodes
        for n in at_risk:
            if flip(lam):
                infected.add(n)

        # verify that there are still infected nodes
        if not infected:
            break

    return infected_nums
