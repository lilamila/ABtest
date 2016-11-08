---
title: "ABTesting"
author: "Marie Leaf"
date: "May 31 2016"
output: html_document
---

#Final Project 

Items that should be copied from your answers to the quizzes should be given in blue.

###Experiment Design

###Metric Choice

From the list of available metrics, I detail below how each was chosen as either an invariant or evaluation metric.

* **# Cookies**
* **# UserIDs**
* **# Clicks**
* **Click-through-probability**
* **Gross Conversion**
* **Retention**
* **Net Conversion**
* 

For each metric, explain both why you did or did not use it as an invariant metric and why you did or did not use it as an evaluation metric. Also, state what results you will look for in your evaluation metrics in order to launch the experiment.

###Measuring Standard Deviation
The metrics' baseline values are used to analytically estimate the standard deviation (SD) of the selection evaluation metrics. A binomial distribution is assumed where SD = sqrt((p*(1-p)/N))

**Gross conversion:**

**Net conversion:**

**# UserIDs**


List the standard deviation of each of your evaluation metrics. (These should be the answers from the "Calculating standard deviation" quiz.)

For each of your evaluation metrics, indicate whether you think the analytic estimate would be comparable to the the empirical variability, or whether you expect them to be different (in which case it might be worth doing an empirical estimate if there is time). Briefly give your reasoning in each case.

###Sizing
**Number of Samples vs. Power**
Indicate whether you will use the Bonferroni correction during your analysis phase, and give the number of pageviews you will need to power you experiment appropriately. (These should be the answers from the "Calculating Number of Pageviews" quiz.)

**Duration vs. Exposure**
Indicate what fraction of traffic you would divert to this experiment and, given this, how many days you would need to run the experiment. (These should be the answers from the "Choosing Duration and Exposure" quiz.)

Give your reasoning for the fraction you chose to divert. How risky do you think this experiment would be for Udacity?

###Experiment Analysis
**Sanity Checks**
After collecting experiment data, it is important to run sanity check tests to confirm the internal validity of the experiment. By analyzing the invariant metrics, we can confirm that the EXP(experiment) and CONT(control) conditions are comparable.
I compare the number of *cookies* and *clicks* on the start free trail button across the EXP and CONT groups. We assume the split is 50%

*assuming bi distro and 95% confidence interval for the invariant metrics the below list shows the calculated results

number of cookies: passed - lower bound 0.4988/ upper bound = 0.5012/ observed 50.5006

number of clicks on start free trial passwed lower bound = .......

for both invariant metrics we are within the 95% confidence interval and therefore the experiment passes the sanity check
*

For each of your invariant metrics, give the 95% confidence interval for the value you expect to observe, the actual observed value, and whether the metric passes your sanity check. (These should be the answers from the "Sanity Checks" quiz.)

For any sanity check that did not pass, explain your best guess as to what went wrong based on the day-by-day data. Do not proceed to the rest of the analysis unless all sanity checks pass.

###Result Analysis
Effect Size Tests
For each of your evaluation metrics, give a 95% confidence interval around the difference between the experiment and control groups. Indicate whether each metric is statistically and practically significant. (These should be the answers from the "Effect Size Tests" quiz.)

gross conversion
....

the gross conversion is statistically significant (does not include the zero calue and practically significant)
Sign Tests

the sign test is a special case of the binomial case where your theory is that the two outcomes have equal probabilities

For each of your evaluation metrics, do a sign test using the day-by-day data, and report the p-value of the sign test and whether the result is statistically significant. (These should be the answers from the "Sign Tests" quiz.)

Summary

the results of both tests (effect size and sign tests) agree with each other. as expected, the gross conversion was lower in the experiment condition than in the controlled condition. however, the net conversion decreased too, but not statistically significant.
considering the practically significant for net conversion, which is within the confidence intercal, there might be a big enough inpact on the businesss cause by the decrease of net conversion through the additional 'popup' question

i did not use the bonferroni corrected because both evaluatioan metrics need to be valid, 
Valid meaning the gross conversion should decrease significantly, but at the same time net conversion should not decrease significantly.
bonferroni correction in this case would be too conservative


State whether you used the Bonferroni correction, and explain why or why not. If there are any discrepancies between the effect size hypothesis tests and the sign tests, describe the discrepancy and why you think it arose.

Recommendation
Make a recommendation and briefly describe your reasoning.

Follow-Up Experiment
Give a high-level description of the follow up experiment you would run, what your hypothesis would be, what metrics you would want to measure, what your unit of diversion would be, and your reasoning for these choices.