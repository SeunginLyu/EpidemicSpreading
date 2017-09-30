"""
Generates various network topologies with NetworkX.
"""

import networkx as nx
import numpy as np
import random


def flip(p):
    return np.random.random() < p


def gen_ER_graph(n, p):
    """ all possible edges have p probability of manifesting """
    def random_pairs(nodes, p):
        for i, u in enumerate(nodes):
            for j, v in enumerate(nodes):
                if i > j and flip(p):
                    yield u, v

    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(random_pairs(nodes, p))
    return G


# WS
def gen_WS_graph(n, k, p, mode="lattice"):
    """ ring lattice with even k, and probability p of random rewiring """

    def adjacent_edges(nodes, halfk):
        """Yields edges between each node and `halfk` neighbors.
        halfk: number of edges from each node
        """
        n = len(nodes)
        for i, u in enumerate(nodes):
            for j in range(i+1, i+halfk+1):
                v = nodes[j % n]
                yield u, v

    def ring_lattice(n, k):
        """Makes a ring lattice with `n` nodes and degree `k`.

        Note: this only works correctly if k is even.

        n: number of nodes
        k: degree of each node
        """
        G = nx.Graph()
        nodes = range(n)
        G.add_nodes_from(nodes)
        G.add_edges_from(adjacent_edges(nodes, k//2))
        return G

    def regular_graph(n, k):
        def opposite_edges(nodes):
            for i, u in enumerate(nodes):
                j = i + len(nodes)//2
                v = nodes[j % len(nodes)]
                yield u, v

        """Takes n,k and returns a regular graph(every node is degree k)"""
        if(k >= n or (n % 2 == 1 and (k % 2 == 1))):
            raise ValueError('cannot make a regular graph with given n, k')
        else:
            G = nx.Graph()
            G.add_nodes_from(range(n))
            G.add_edges_from(adjacent_edges(range(n), k//2))
            if (k % n != 0):  # when even number of nodes
                G.add_edges_from(opposite_edges(range(n)))
            return G

    def rewire(G, p):
        nodes = set(G.nodes())
        for edge in G.edges():
            if flip(p):
                u, v = edge
                choices = nodes - {u} - set(G[u])
                new_v = random.choice(tuple(choices))
                G.remove_edge(u, v)
                G.add_edge(u, new_v)

    if(mode == 'lattice'):
        ws = ring_lattice(n, k)
    else:
        ws = regular_graph(n, k)

    rewire(ws, p)
    return ws


def gen_BA_graph(n, k):
    """ generate one node at a time,
    connecting preferentially to higher degree nodes """
    return nx.barabasi_albert_graph(n, k)


def load_graph(filename):
    """predetirmined graph (this will be used to grab the facebook graph) """
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)


# graph = gen_ER_graph(10, 0.3)
# graph = gen_WS_graph(10, 4, 0.3, mode='regular')
