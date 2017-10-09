# Simulation of Epidemic Spreading in Varying Network Topologies
## by Duncan Hall and Seungin Lyu


### Abstract



"Why do epideimc spreading models with local connectivity contradict with the statistical observations of virus epidemics that viruses are able to pervade and spread much slower than exponentially, and saturate to a low level of persistence?".

"how viral prevalence and persistence/survival changes in a real-world graph?""



In this report, we replicate an experiment by Pastor-Satorras and Vespignani[1] in an effort to answer the question


We investigate the phenomenon of epidemic spreading by running susceptible-infected-susceptible(SIS) model simulation on varying network topologies including the Erdos-Renyi graph, Watts and Strogatz graph, and Barabasi and Albert’s power law graph. We




### Introduction



### Methods




### Results



### Conclusions

for epidemic threshold: we see that the virus dies out on BA graphs too, but increasing the number of nodes fixes that. Maybe it doesn't fix on non-scale-free graphs? we need to change ER graph generation to test this though


### Bibliography

#### 1. [Epidemic spreading in scale-free networks](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_spreading_in_SF_networks.pdf)

Pastor-Satorras, R., & Vespignani, A. (2001). Epidemic spreading in scale-free networks. Physical review letters, 86(14), 3200.

Pastor-Satorras and Vespignani  designed a model for the spreading of infections on scale-free networks. They applied the susceptible-infected-susceptible (SIS) epidemiological model on scale-free graphs (Barabasi and Albert). They believe that models with SIS applied to Euclidean lattices, ER graphs, and WS graphs aren’t completely adequate to represent the real phenomenon because the end behavior after time *t* eventually yields either complete extinction or complete prevalence of a computer virus depending on whether the effective spreading rate is greater or less than the epidemic threshold. They discover the absence of the epidemic threshold in scale-free networks and conclude that “infections can proliferate on these scale-free networks whatever spreading rates they may have. These very bad new are, however, balanced by the exponentially small prevalence for a wide range of spreading rate”.

#### 2. [Epidemic spreading in Real Networks : An Eigenvalue Viewpoint](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_threshols_real_networks_eignevalue.pdf)

Wang, Y., Chakrabarti, D., Wang, C., & Faloutsos, C. (2003, October). Epidemic spreading in real networks: An eigenvalue viewpoint. In Reliable Distributed Systems, 2003. Proceedings. 22nd International Symposium on (pp. 25-34). IEEE.

Wang, Yang and Chenxi Wang proposed a ‘general’ epidemic threshold condition that applies to arbitrary graphs and prove that the epidemic threshold is closely related to the largest eigenvalue of its adjacency matrix under reasonable approximations. They point out that the model proposed by Pastor-Satorras and Vespignani is only limited to the BA graph and only works heavily under the assumption that gamma = 3 when *P(k) = k^(-gamma)* (*P(k)* is the probability that a node has *k* links). They validate their epidemic spreading model on both homogeneous graphs like ER graph and power-law scale free graphs like the BA graph. They conclude that their threshold condition holds for arbitrary graphs by validating their model through extensive experiments on real and synthesized graphs.


#### 3. [Epidemic Thresholds in Real Networks](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_thresholds_real_netowkrs.pdf)

Chakrabarti, D., Wang, Y., Wang, C., Leskovec, J., & Faloutsos, C. (2008). Epidemic thresholds in real networks. ACM Transactions on Information and System Security (TISSEC), 10(4), 1.
Chicago


They present a new analytic model called NLDS(nonlinear dynamic system) that makes no assumptions about the network topology and show that their model performs as well or better than the previous models that are targeted specifically to fit certain special case graphs like ER, WS, and BA graphs. This is an improved version of <i>Epidemic Spreading in Real Networks : An Eigenvalue Viewpoint</i> (written five years later by almost the same group of author). They conclude that their threshold condition can be used to design new network topologies that are more resistant to viruses.
