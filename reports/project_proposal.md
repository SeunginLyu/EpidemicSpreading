# Simulation of Epidemic Spreading in Varying Network Topologies
## by Duncan Hall and Seungin Lyu

### Abstract

We investigate the phenomenon of epidemic spreading by running SIS model simulation on varying network topologies including the Erdos-Renyi graph, Barabasi and Albert’s power law graph. We experiment with the epidemic threshold that yields different steady states on different network topologies. We plan to animate the dynamic states of the epidemic spreading using networkX in addition to replicating the plots that are present in the papers listed in our annotated bibliography so that we get a better visual sense of the process.

### Annotated Bibliography

#### 1. [Epidemic spreading in scale-free networks](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_spreading_in_SF_networks.pdf)

Pastor-Satorras, Romualdo, and Alessandro Vespignani. "Epidemic spreading in scale-free networks." Physical review letters 86.14 (2001): 3200.

Pastor-Satorras and Vespignani  designed a model for the spreading of infections on scale-free networks. They applied the susceptible-infected-susceptible(SIS) epidemiological model on scale-free graphs(Barabasi and Albert). They believe that models with SIS applied to Euclidean lattices, ER graphs, and WS graphs aren’t completely adequate to represent the real phenomenon because the end behavior after time t eventually yields either complete extinction or complete prevalence of a computer virus depending on whether the effective spreading rate is greater or less than the epidemic threshold. They discover the absence of the epidemic threshold in scale-free networks and conclude that “infections can proliferate on these scale-free networks whatever spreading rates they may have. These very bad new are, however, balanced by the exponentially small prevalence for a wide range of spreading rate”.

#### 2. [Epidemic spreading in Real Networks : An Eigenvalue Viewpoint](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_threshols_real_networks_eignevalue.pdf)

Wang, Yang, et al. "Epidemic spreading in real networks: An eigenvalue viewpoint." Reliable Distributed Systems, 2003. Proceedings. 22nd International Symposium on. IEEE, 2003.

Wang, Yang and Chenxi Wang proposed a ‘general’ epidemic threshold condition that applies to arbitrary graphs and prove that the epidemic threshold is closely related to the largest eigenvalue of its adjacency matrix under reasonable approximations. They point out that the model proposed by Pastor-Satorras and Vespignani is only limited to the BA graph and only works heavily under the assumption that gamma = 3 when P(k) = k^(-gamma) (P(k) is the probability that a node has k links). They validate their epidemic spreading model on both homogeneous graphs like ER graph and power-law scale free graphs like the BA graph. They conclude that their threshold condition holds for arbitrary graphs by validating their model through extensive experiments on real and synthesized graphs.




#### 3. [Epidemic Thresholds in Real Networks](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_thresholds_real_netowkrs.pdf)

Chakrabarti, Deepayan, et al. "Epidemic thresholds in real networks." ACM Transactions on Information and System Security (TISSEC) 10.4 (2008): 1.

They present a new analytic model called NLDS(nonlinear dynamic system) that makes no assumptions about the network topology and show that their model performs as well or better than the previous models that are targeted specifically to fit certain special case graphs like ER, WS, and BA graphs. This is an improved version of <i>Epidemic Spreading in Real Networks : An Eigenvalue Viewpoint</i>, written five years later by almost the same group of author. They conclude that their threshold condition can be used to design new network topologies that are more resistant to viruses.


### Scope of the Simulation

We plan to use a susceptible-infected-susceptible (SIS) disease model in our simulation, and will examine the spread of that disease through ER, WS, and SF topologies. In ER and WS graphs we expect the infected fraction of nodes to be unstable and either go to zero as the disease is exterminated or the entire network to become infected. In a SF topology however, we expect to see an equilibrium reached with a constant fraction of infected nodes. Below are some sketches of the graphs we anticipate:

![Anticipated Graphs](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/resources/epidemic_simulation_graphs.JPG)

As extensions we would like to model the interaction of multiple diseases, with a variety of interaction mechanisms. Our ideas include a disease which makes nodes more susceptible to another disease, a disease with cures the other, or mutually exclusive diseases. We do not yet know what to expect from these experiments, but it would be cool to visualize the results over time with networkx’s imaging functions.


### First Steps

Before diving into implementation we feel our time would be well spent going over the mathematical explanations in one of our auxiliary papers to get a different perspective on the same subject and a similar experiment. We anticipate doing this before our Friday class, and then beginning implementation that weekend. Most of the code to generate our networks can be repurposed from our reading journals, and we plan to work together to implement the disease transfer and break things into small chunks as we go. This will be made effective by using a plugin for Atom called atom-pair which allows floobits-style remote parallel file editing in real time.
