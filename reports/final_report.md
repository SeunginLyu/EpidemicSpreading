# Simulation of Epidemic Spreading in Scale-free Networks
## by Seungin Lyu and Duncan Hall


### Abstract

How prevalent is an epidemic spreading in scale-free networks? What is the survival probability of viruses over a range of time? We answer these questions by replicating an experiment by Pastor-Satorras and Vespignani [1] which involves running the susceptible-infected-susceptible (SIS) model on the Barabasi and Albert's (BA) power law graphs. We apply their methodology to a Facebook dataset [4] to further explore their model on a real-world network. We show that viruses with any spreading rate reach a steady state of prevalence on scale-free networks. We conclude that scale-free networks are prone to epidemic spreading regardless of the spreading rate.

### Replication of Pastor-Satorras and Vespignani's experiment

Pastor-Satorras and Vespignani originally asked the question "why do epidemic spreading models with local connectivity contradict with the statistical observations of virus epidemics that viruses are able to pervade and spread much slow than exponentially, and saturate to a low level of persistence?" [1]. After observing and analyzing data of Virus Bulletin, they claimed that previous spreading models with local connectivity like ER graph and WS graph don't illustrate the scale-free nature of the real world networks such as the Internet. While looking for an explanation and designing a model that represents the real world, they hypothesize that running SIS model simulation on Barabasi and Albert's graph will illustrate the exponential tail of virus prevalence. To find how prevalent epidemic spreading is in scale-free graphs, we replicate the experiment that they conducted with the BA graph.

We use the susceptible-infected-susceptible (SIS) epidemic model as our primary means of simulation. SIS epidemic model mimics infections such as influenza that do not give immunization upon recovery from infection, so individuals become susceptible again. In SIS model, an infected node recovers with probability (rate) `σ`, and susceptible nodes are infected if at least one neighbor is infected with probability (rate) `µ`. We define the spreading rate `λ = µ/σ`. We are able to fix `σ = 1` without loss of generality [1]. Note that updating the status of all nodes is done in parallel; that is, to update the status for time `t`, only statuses of time `(t-1)` of the nodes are considered.

We define a list of terms in our experiment. The virus prevalence `'ρ' is the fraction of infected nodes at any time`. In this experiment, we examine the prevalence only when the simulation enters a steady state with an oscillating fraction of infected nodes at a constant level. We evaluate the steady-state prevalence 'ρ' by calculating the mean of infected nodes at time step t over multiple trials. Additionally, We calculate surviving probability P<sub>s</sub>(t) as `number of trials with a surviving virus at time step t / total number of trials conducted`.

We use a BA graph generated from the NetworkX's `barabasi_albert_graph(n, k)` function. We set the number of edges to attach from a new node to existing nodes k = 3, which is equivalent to an average node degree of 6. We use the number of nodes N ranging from 10<sup>3</sup> to 8.5×10<sup>6</sup>.

We show the results of our simulation in Figure 1 and Figure 2.


| ![Figure 11](../resources/figure11.png)  ![Figure 1](../resources/figure1.png)


*Figure 1. : (left) Pastor-Satorras and Vespignani's original figure of prevalence ρ as a function of 1/λ for different network sizes: N = 10<sup>5</sup> (+), N = 5 × 10<sup>5</sup>(◻), N = 10<sup>6</sup> (×), N = 5 × 10<sup>6</sup> (○), and N = 8.5 × 10<sup>6</sup> (◇). The full line is a fit to the form ρ ∼ exp(−C/λ) [1]; (right) We replicate the original plot with our own simulation. We use the identical semi-log axis as used in the original. Each color corresponds to a network size in the original experiment.(from red : N = 10<sup>5</sup> to sky blue : N = 8.5 × 10<sup>6</sup>). The prevalence constant C, or the slope of the linear fitting line is -0.38. We take the mean of infected nodes at t = 20.*


![Figure 21](../resources/figure21.png) ![Figure 2](../resources/figure22.png)

*Figure 2. : (left) Pastor-Satorras and Vespignani's original figure of the surviving probability P<sub>s</sub>(t) for a spreading rate λ = 0.065 in scale-free networks of size N = 5 × 10<sup>5</sup> (◻), N = 2.5 × 10<sup>4</sup> (◇), N = 1.25 × 10<sup>4</sup> (△), and N = 6.25 × 10<sup>3</sup> (○) [1]; (right). We replicate the original plot with our own simulation. Note we run the simulation for 50 time steps and run 100,000 trials in total. While the horizontal steady state for N = 5 × 10<sup>5</sup> matches that of the original plot, we observe quantitative differences for all other network sizes.*


<br>

In Figure 1, we illustrate that viruses with spreading rate ranging from 1/22 to 1/7 reach a steady state of prevalence `ρ ~ exp(-C/λ)` on the BA graph. We confirm that our replicated plot of ρ as a function of 1/λ quantitatively agrees with the original. One interpretation of the plot shown in Figure 1 is that viruses persist at a low prevalence that is always greater than 0(finite prevalence) in a BA graph regardless of its size. Another interpretation is that the virus prevalence decays inversely proportional to the sreading rete. So the faster the spreading rate is, the lower the prevalence is going to be.

In Figure 2, we observe that the behavior of surviving probability follows a sharp initial exponential drop, a trend which agrees with our interpretation of the prevalence graph. The virus prevalence plots in Figure 1 and the surviving probability plots in Figure 2 are compatible because, for a fixed spreading rate (λ = 0.065), the surviving probability must proportionally decrease as the network size increases to yield the same level of virus prevalence for all network sizes. While we confirm a qualitative match between the original figure and our result of the simulation, we observe a quantitative difference. The surviving probability in our plot for N < 5 × 10<sup>5</sup> decays more rapidly, roughly twice as faster than that of the original. We do observe in our simulation that running more trials results in a graph that is more quantitatively similar to the original. So this quantitative difference potentially comes from an insufficient number of trials(100,000) conducted in our simulation. However, we are unable to identify the exact cause of this discrepancy because Pastor-Satorras and Vespignani [1] did not explicitly mention the number of trials they used.


### Going Beyond: SIS model simulation on Facebook network

To extend Pastor-Satorras and Vespignani's experiment beyond the specific BA graph, we apply the same implementation of the SIS model simulation to a Facebook network with 88234 edges and 4039 nodes. Assuming that the Facebook graph is similar to the BA graph, we expect the same `ρ ~ exp(-C/λ)` prevalance plot as shown in Figure 1.

We observe that running the same simulation on the Facebook data yields the result shown in Figure 3. We confirm that the result qualitatively matches the prevalence plot shown in Figure 1 but quantitatively differs in regards to the slope of the fitting line and the prevalence level.

We know from ThinkComplexity that a BA graph that resembles the Facebook dataset with 88374 edges and 4039 nodes differs greatly when we take a look at the clustering coefficients. The clustering coefficient is 0.037 for the BA graph and 0.061 for the Facebook graph [5]. Assuming that the one of the primary differences between the BA graph and the Facebook graph is the clustering coefficient, we can infer that the difference in the clustering coefficient contributes to the quantitative discrepancy shown in Figure 3. Even if the assumption is not completely true, we can still assume that the clustering coefficient is one of the major factors that contribute to the higher prevalence level and the relatively low prevalence constant C compared to the BA graph.

With higher prevalence level, viruses can stay more prevalent in the Facebook network with more infected nodes than in the BA graph. With a smaller value of the prevalence constant C, the change in spreading rate has less effect on exponentially decaying prevalence. So viruses can pervade in the Facebook network more dominantly than in the BA graph only if we consider this model valid for the Facebook network.



![Figure 3](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/resources/figure3.png)

*Figure 3. We run the SIS model simulation on the Facebook data provided by SNAP. We run 100 trials for each spreading rate until time step 50. The prevalence constant C or the slope of the linear fitting line is 0.11 which is 0.27 less than that of the BA graph in Figure 1. The prevalence level is also significantly higher by a factor of roughly 100.*


### Conclusion

We conclude that scale-free networks are prone to epidemic spreading regardless of the spreading rate because there always exists a finite prevalence that is greater than zero. However, the epidemic prevalence decays exponentially as the spreading rate increases, so the epidemic prevalence is low for a wide range of spreading rate. In other words, only a small number of nodes are going to be infected at a moment for most spreading rates, but the epidemic will defeintely continue pervade. We also identified a potential positive correlation between the epidemic prevalence and the clustering coefficient of a network by investigating the SIS model on the Facebook network. For future works, we suggest you further explore the topic of network clustering to verify the relationship between the epidemic prevalence and the clustering coefficient of a network.

### Bibliography

#### [1]. [Epidemic spreading in scale-free networks](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_spreading_in_SF_networks.pdf)

Pastor-Satorras, R., & Vespignani, A. (2001). Epidemic spreading in scale-free networks. Physical review letters, 86(14), 3200.

Pastor-Satorras and Vespignani designed a model for the spreading of infections on scale-free networks. They applied the susceptible-infected-susceptible (SIS) epidemiological model on scale-free graphs (Barabasi and Albert). They believe that models with SIS applied to Euclidean lattices, ER graphs, and WS graphs aren’t completely adequate to represent the real phenomenon because the end behavior after time *t* eventually yields either complete extinction or complete prevalence of a computer virus depending on whether the effective spreading rate is greater or less than the epidemic threshold. They discover the absence of the epidemic threshold in scale-free networks and conclude that “infections can proliferate on these scale-free networks whatever spreading rates they may have.

#### [2]. [Epidemic spreading in Real Networks : An Eigenvalue Viewpoint](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_threshols_real_networks_eignevalue.pdf)

Wang, Y., Chakrabarti, D., Wang, C., & Faloutsos, C. (2003, October). Epidemic spreading in real networks: An eigenvalue viewpoint. In Reliable Distributed Systems, 2003. Proceedings. 22nd International Symposium on (pp. 25-34). IEEE.

Wang, Yang, and Chenxi Wang proposed a ‘general’ epidemic threshold condition that applies to arbitrary graphs and proves that the epidemic threshold is closely related to the largest eigenvalue of its adjacency matrix under reasonable approximations. They point out that the model proposed by Pastor-Satorras and Vespignani is only limited to the BA graph and only works heavily under the assumption that gamma = 3 when *P(k) = k^(-gamma)* (*P(k)* is the probability that a node has *k* links). They validate their epidemic spreading model on both homogeneous graphs like ER graph and power-law scale-free graphs like the BA graph. They conclude that their threshold condition holds for arbitrary graphs by validating their model through extensive experiments on real and synthesized graphs.


#### [3]. [Epidemic Thresholds in Real Networks](https://github.com/SeunginLyu/EpidemicSpreading/blob/master/papers/epidemic_thresholds_real_netowkrs.pdf)

Chakrabarti, D., Wang, Y., Wang, C., Leskovec, J., & Faloutsos, C. (2008). Epidemic thresholds in real networks. ACM Transactions on Information and System Security (TISSEC), 10(4), 1.
Chicago

They present a new analytic model called NLDS(nonlinear dynamic system) that makes no assumptions about the network topology and show that their model performs as well or better than the previous models that are targeted specifically to fit certain special case graphs like ER, WS, and BA graphs. This model is an improved version of <i>Epidemic Spreading in Real Networks: An Eigenvalue Viewpoint</i> (written five years later by almost the same group of the author). They conclude that their threshold condition can be used to design new network topologies that are more resistant to viruses.


#### [4]. [SNAP Facebook Dataset](https://snap.stanford.edu/data/egonets-Facebook.html)
Leskovec, Jure, Stanford University(2012)
[https://snap.stanford.edu/data/egonets-Facebook.html](https://snap.stanford.edu/data/egonets-Facebook.html)

#### [5]. Downey, A. B. (2016). Think complexity 2e. " O'Reilly Media, Inc.".
[http://greenteapress.com/complexity2/html/index.html](https://snap.stanford.edu/data/egonets-Facebook.html)
