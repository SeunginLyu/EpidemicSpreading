## Check-in Notes


### Expreiment Replication 1

* What experiment are you replicating?   Who did it?  Any relevant background on the people or the publication?


* What question was their experiment intended to answer?  Is it a prediction, explanation, or design question?
 * Why do epideimc spreading models with local connectivity contradict with the statistical observations of virus epidemics that viruses are able to pervade and spread much slow than exponentially, and saturate to a low level of persistence?
  * (looking for an explanation and desgining a model that represents the real phenomenon)

* How did they go about answering it?
 * Hypotehsis : "What is the effect of scale-free nature of networks on epidemic spreading?"(explanation)
 * first observe and analyze data reported by Virus Bulletin - > exponential tail(SF proproperty)
  * ER, WS (does not capture Scale free nature of the internet ) ->>>  simulations & analysis of SIS model on SF graphs(BA graph)
 * BA graph specifications :
  * k = 3, (<k> = 6)
  * N = 10^3 to 8.5 * 10^6
  * studied virus prevalence : density of infected nodes rho in surviving infections
    (when the simulation enters steady sate with constant average dneisty of infected nodes)
   - 1) initially infect half of the nodes
   - 2) SIS model with parallel updating each time stpe t
     * SIS model :
      * An infected node recovers with probabiliy(rate) sigma (they set it to = 1)
      * An infected node attemps to infect each neighbor with probability(rate) v
      * Note : Updating of the nodes statuse are done in parallel, that is,
        to update the status for time t only statuses of time t-1 of the other nodes are considered.
   - surviving probability P_s(t) : virsuses still alive at time t after their birth / total number of observed virsuses
* What was the result of the experiment?
 *  
  absence of an epidemic threshold
 *  


* How does this result answer the question?
  * SF networks are prone to the spreading and the persistence of infections whatever "spreading rate the epidemic agents possess"

* Have you replicated the experiment?  Any important details to report?

* Did the experiment replicate?  If so, how do you show that your results agree with theirs?  If not, do you understand why not?

### Plans for Extension

* What question will your experiment answer?

* What methodological changes will you have to make?

* What might the results look like?

* How will you interpret the results?


### Notes

* key words :
  - the average liftime and prevalence of viral strains
  - power-law distribution with gamma from 2 ~ 3
  - local clustering
  - "nonequilibrium phase transitions"
  - effective spreading rate gamma = mu / sigma
  - in models with local connectivity, nonzero epideimc threshold exists
    - if gamma above gamma_c, infection become persistent
    - if gamma below gamma_c, infection dies out exponentially.
