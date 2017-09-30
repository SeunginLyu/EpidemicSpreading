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

    # initial state
    infected = set(random.sample(graph.nodes(), int(graph.number_of_nodes() * rho_0)))

    # begin time steps
    for _ in range(time_steps):

        for n in graph.nodes():

            # susceptible nodes are infected with probability lambda if they
            #   have at least one infected neighbor.
            if n not in infected:
                for m in graph[n]:

                    if m in infected:
                        if flip(lam):
                            infected.add(n)
                        # we only make one roll per susceptible node
                        break

            # infected nodes are cured with a probability of d = 1
            else:
                infected.remove(n)

        # verify that there are still infected nodes
        if not infected:
            break

    return len(infected) / float(graph.number_of_nodes())
