Question -> clear
methodology -> clear
Figure -> Wrong figure referencing 1.a, 1.b
Graphs -> Only numbers but no interpretation
-> Interpret the interpretation in the original paper
->Ackknoledgement of what it is not completely replicated quantitatively (Don't ignore it)

-> Plot Legends and Keys (for colors and different shapes)
-> Reiterate the question one more time
-> SIS model background -> EXPLAIN!!!!
-> Our Experiment -> Present Tense, Their experiement : Past Tense
-> Cite the Facebook graph data.

### Emily Lepert
#### Question:  What is your understanding of the experiment the team is replicating?  What question does it answer?  How clear is the team's explanation?
The experiment is investigating how viruses spread throughout different network topologies and what the survival rate for viruses is. They want to see how the method proposed by the authors of the paper holds up on different network topologies. The explanation is clear. They have questions, an explanation on how they extend the model, and the main take aways in the abstract so it's easy to understand what their claiming.

#### Methodology: Do you understand the methodology?  Does it make sense for the question?  Are there limitations you see that the team did not address?
Methodology is clear, variables are explained.

#### Results: Do you understand what the results are (not yet considering their interpretation)?  If they are presented graphically, are the visualizations effective?  Do all figures have labels on the axes and captions?
Figure naming is not clear. "We show the results of our simulation in Figure 1.2 and Figure 2.2 in comparison to the original plots [1] in Figure 1.1 and Figure 1.2 respectively." They mention Figure 1.2 twice but never 2.1, so it is confusing.

Captions and axes are present. Caption explains what each graph is.

#### Interpretation: Does the draft report interpret the results as an answer to the motivating question?  Does the argument hold water?
There is very little interpretation for the experiment. It would be nice to have some explanation of what the results mean for both the replication and the extension. Link the numerical results they generate to the supposed interpretation of the paper as well as the extension's interpretation. There shouldn't be a need to read the original paper to interpret the results. I would relate the results back to the questions.

#### Replication: Are the results in the report consistent with the results from the original paper?
Figures 2.1 and 2.2 look the same qualitatively but they are not quantitatively similar. They write that they were replicating it qualitatively, but they only write this: "to replicate Figure 2.1 up to 50 time steps as shown in Figure 2.2." as an interpretation of the results. It would be good to have some explanation as to why they are not quantitatively similar. I understand that it was run for 50 times steps, but as a reader I would expect to see the first half of the paper's graph rather than different numbers entirely.

#### Extension: Does the report explain an extension to the original experiment clearly?  Is it a sensible extension in the sense that it has the potential to answer an interesting question that the original experiment did not answer?
I had to go back to look at what the questions were by the time I reached the extension. It would be good to reiterate the relationship between the extension and the original question. The extension seems sensible in terms of giving some interesting insight. There isn't currently any analysis of the extension results, but as long as those reveal some insight, the extension should be good.

#### Progress: Is the team roughly where they should be at this point, with a replication that is substantially complete and an extension that is clearly defined and either complete or nearly so?
The replication seems to be mostly complete (should add interpretation). What the extension entails is clear and looks like it is part of the way through.

#### Presentation: Is the report written in clear, concise, correct language?  Is it consistent with the audience and goals of the report?  Does it violate any of the recommendations in my style guide?
There is not a lot of background on the SIS model. As a reader who knows about the class, I still don't know what an SIS model is (I can infer from the paper), so a short explanation beyond what mathematical terms mean might be useful.
There isn't much explicitly written about motivation but the question is interesting. Perhaps there isn't much more that needs to be written.

#### Mechanics: Is the report in the right directory with the right file name?  Is it formatted professionally in Markdown?  Does it include a meaningful title and the full names of the authors?  Is the bibliography in an acceptable style?
This all looks good.


# Draft Review of Simulation of Epidemic Spreading in Various Network Topologies

### Vicky McDermott

## Question:
### What is your understanding of the experiment the team is replicating?  What question does it answer?  How clear is the team's explanation?
The experiment this team is replicating investigated the survival probability of viruses over a range of time. It answers the question of how prevalent epidemic spreading affects various network topologies. It also answers the question of what the survival probability of these viruses is over time for various spreading rates. The setup and introduction of the team's question seems to me to be fairly clear. I think they drift away from the question at hand bit later in the paper when they start to focus more on whether or not the spreading of the disease reaches a steady state, a related (but different) question of interest.

## Methodology:
### Do you understand the methodology?  Does it make sense for the question?  Are there limitations you see that the team did not address?
The methodology does seem to make to make sense for the question they are answering. They did a good job of describing the susceptible-infected-susceptible model that they used for their experiment. I would like to hear a little more about what the steady state prevalence for a disease is defined as. Does this mean that the same number of people are getting healthy and getting sick? Or something different? Other than that everything seems fairly clear, and I think it would be easy enough for future investigators to replicate their work.

## Results:
### Do you understand what the results are (not yet considering their interpretation)?  If they are presented graphically, are the visualizations effective?  Do all figures have labels on the axes and captions?
The results seem to make sense and the replication of the graph plotting 1/spreading rate by the disease prevalence at steady state seems to be consistent with the graph they are replicating. Although I understand they only did 50 time steps for the graph of surviving probability over time, whereas the graph they are replicating has 100 time steps, I would like to see some more explanation of the quantitative differences between their graph and the original graph. The surviving probability in the original graph does not go below 10^-3 in the first 50 time steps but 3 out of 4 of their lambda values do go below 10^-3 in the replicated graph in the first 50 time steps. All of the graphs are nicely labeled and include captions. I like the colors in the graphs but I think it is sometimes hard to understand what the different colors are representing. Having a key on the figures might be a nice addition.

## Interpretation:
### Does the draft report interpret the results as an answer to the motivating question?  Does the argument hold water?
It seems as if the draft report has not really started interpreting the results yet. They have presented the results of their replication and are in the process of generating more results for their extension. I would love to see more of an interpretation of their replicated results. I know that the replication has probably already been interpreted by the authors of the paper they are replicating, but as a person who has not read that paper, I would love to see some more interpretation of the results. Especially in the places where their graphs differ from the original graphs, an explanation or interpretation of why this might be the case would be really nice.

## Replication:
### Are the results in the report consistent with the results from the original paper?  If so, how did the
It seems like the results in the report are mostly consistent with the results from the original paper. Again, I would like to see some more interpretation and explanation of the discrepancies I am seeing between their graphs and the original graph. Qualitatively though, the results look to be very similar making me think the replication is in fact accurate.

## Extension:
### Does the report explain an extension to the original experiment clearly?  Is it a sensible extension in the sense that it has the potential to answer an interesting question that the original experiment did not answer?
The extension has been explained clearly. I like how the authors came up with a hypothesis and are now testing reasons why their original hypothesis might not be correct. I think generating these additional graphs using this model will be a very interesting and appropriate extension for their work. It should answer the overall question of how disease spreading works on scale free networks as a whole.

## Progress:
### Is the team roughly where they should be at this point, with a replication that is substantially complete and an extension that is clearly defined and either complete or nearly so?
The progress of the team seems very reasonable to me. They still need to complete their replication but it certainly sounds like they both have a plan and have made a substantial start in implementing their extension. The replication seems to be very nearly done. I would still like to see a little more description and explanation of the discrepancies between their model and the one they are replicating but I think they have made very decent progress and are at a good place for this point in the project.

## Presentation:
### Is the report written in clear, concise, correct language?  Is it consistent with the audience and goals of the report?  Does it violate any of the recommendations in my style guide?
I do not see any obvious violations of the style guide. The report is concise and explains a great deal about their model and about the questions they are answering. There are a few typos and they slip into the past tense a few times but I think this might be ok in the context of the paper. Generally, the language is clear and it seems to me to be well written.

## Mechanics:
### Is the report in the right directory with the right file name?  Is it formatted professionally in Markdown?  Does it include a meaningful title and the full names of the authors?  Is the bibliography in an acceptable style?
Looks like it is located in the proper reports folder. The Markdown formatting looks good to me. The title does a good job of sparking interest and introducing the topic material and the full names of the authors are included in the paper. The bibliography looks to me to be in an acceptable style.
