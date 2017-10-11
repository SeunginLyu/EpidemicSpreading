1. Question :
    * I can't clearly figure out what question you are asking from the abstract. I assume you are asking "does Google have the best search engine algorithm?" from your title. But it seems like you replicate Page and Brin's pagerank paper to determine whether their algorithm is the "best". I feel like the title is misleading and does not represent the paper comprehensively.
    * I am having trouble understanding the mathmatical definitions frequently used in this paper. What are back links and links? How does page rank algorithm work? What is a collaboration network?
    * You do mention the definition of betweenness centrality as "a metric for determining the centrality of nodes in a graph based on shortest path lengths", but I only have a vague understanding of the concept. How do you evaluate the centrality of nodes?

2. Methodology:
      * "We assumed that if there was a high correlation between the page rank probability distribution of a node and the betweenness centrality of the same node, then the page rank algorithm would be an accurate way of determining which websites are most popular."
      * I assume that you are comparing the PageRank algorithm with Brandes' optimized algorithm from the paper you are citing, but I don't understand how that answers your question.
      * "...there was high correlation between the probability distribution of page rank and the betweenness centrality of the nodes. "

3. Results:
      * I clearly understand that there is a strong corrleation between the page rank probability and the betweenness centrality for both BA and ER graphs.
      * Titles like "Simulation on BA graph" and "Simulation on ER graph" are missing from the figures.

4. Interpretation:
      * I don't understand your interpretation that "the page rank algorithm would be a good metric to determine which websites should be shown first, since there is a strong correlation between page rank probability and centrality." because I do not intuitively get what centrality is.
      * Even if your interpretation is totally valid(which I believe it is), youur interpretation of the results still does not answer your question "is Google really the best search engine?". I don't think this question can be answered unless you compare all the existing search engines which I believe is way beyond the scope of this project.

5. Replication:
      * The results of page rank algorithm replication are consistent with the results from the original paper.

6. Extension:
      * I see that you are extending your experiment by applying the same methodology used in BA and ER grphs to a collaboration network.
      * I would definetely understand the content better if I was given a brief explanation about what a collaboration network is.
      * I'm not sure if this extension actually helps me answer the original question.

7. Progress:
      * I see that the implementation of the algorithms and simulations is complete. The replication is complete and the extension is complete too. It seems like you are stil working on the interpretation and the conclusion part of the report.

8. Presentation:
    * I see several places where you use the past tense when you could in fact use the present tense instead.
    * I recommend using Figure 1. and Figure 2. instead of saying "The <i> following table </i>shows... <i>and the table after<i>.." I actually got a little confused when read "the first figure, the second figure, and the third figure.."
    * I don't think distinguishing tables and figures is necessary(I would use something like Figure1, Figure2, Figure 3 ...)
    * I do not see any captions for the figures. I believe adding simple descriptions for each figure will help both you and the readers quickly understand the results.
    * I would write "Page and Brin design [1]" instead of "In Page and Brin's paper The PageRank Citation Ranking: Bringing Order to the Web, the two Stanford researchers design"

9. Mechanics:
    * The bibliography does not contain full APA style citations for each entry.
