# Leafer's A/B Testing

Leafer's A/B Testing is a designed A/B test. I chose with metrics to measure and how long the test should be run. The results of an A/B test run by Udacity are analyzed and recommendations on whether or not the changes should be launched are made. Created by [Marie Leaf](https://twitter.com/mariesleaf).


### Table of contents

* [Summary](#summary)
* [Concepts](#concepts)
* [Creator](#creator)
* [Resources](#resources)

### Summary

* [Open the HTML page](index.html).
**Business Goal:** 
Improve student experience by setting expectations of time commitment and improve coach capacity to support students who are likely to complete the course, without detterring students from continuing past free trial.

**Mechanics of UX:** 
Udacity courses currently have two options on the home page: **"start free trial"**, and **"access course materials"**.

If the student clicks *"start free trial"*, they're asked for credit card information, and then enrolled in a free trial for the paid version of the course. After 14 days, they're automatically charged unless they cancel.

If the student clicks *"access course materials"*, they're able to view the videos and take the quizzes for free, but they can't receive coaching support or a verified certificate, and they can't submit their final project for feedback.

**Recommendation**

Although we did see a statistically and practically significant effect on the gross conversion rate by ~2%, this is just an intermediary step and indication of improving the overall experience, (which would be evidenced by an practically significant effect on the **net conversion**). The net conversion difference however was not statistically or fully practically significant in either the Size or Sign tests. However, the net conversion difference does include the negative end of the practical significance boundary, that is, it is possible that net conversion decreased in a way that was practically significant to the business. So it is not advisable to completely dismiss the effectiveness of the change.

From the results we observed, I would recommend re-running the experiment, perhaps slicing by country/other demographic indicator, or changing the wording of the free-trial screener.

### Concepts

Practical/Substanstive Significance
Experiment Ethics
Choosing and characterizing business metrics
Experiment Design

### Creator

**Marie Leaf**

* <https://twitter.com/mariesleaf>
* <https://github.com/mleafer>

### Resources

* [Markov(DP) Substitute in 20-Lines](http://stevehanov.ca/blog/index.php?id=132) (*not used but interesting to note*) 
* [Dynamic Programming Substitute](http://www.win-vector.com/blog/2015/07/dynamic-prog-ab-test-design/)
* [Power & Significance in A/B Testing](http://www.win-vector.com/blog/2014/05/a-clear-picture-of-power-and-significance-in-ab-tests/)
* [Z-score Table](http://www.utdallas.edu/dept/abp/zscoretable.pdf)
* [Sign Test](http://graphpad.com/quickcalcs/binomial1.cfm)

