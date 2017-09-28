"""
Generates various network topologies with NetworkX.
"""

import networkx as nx


# ER
def gen_ER_graph(n, p):
    """ all possible edges have p probability of manifesting """
    pass

# WS
def gen_WS_graph(n, k, p):
    """ ring lattice with even k, and probability p of random rewiring """
    pass

# BA
def gen_BA_graph(n, k):
    """ generate one node at a time, connecting preferentially to higher degree nodes """
    pass

# predetirmined graph (this will be used to grab the facebook graph)
def load_graph(filename):
    pass

# all functions that return networkx graph object
# verify specific variation of each network with 1st paper.
