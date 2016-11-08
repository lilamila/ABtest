


# A/B Testing Udacity's Course Onboarding
Author: Marie Leaf 
Date: June 14th, 2016

**Business Goal:** 
Improve student experience by setting expectations of time commitment and improve coach capacity to support students who are likely to complete the course, without detterring students from continuing past free trial.

**Mechanics of UX:** 
Udacity courses currently have two options on the home page: **"start free trial"**, and **"access course materials"**.

If the student clicks *"start free trial"*, they're asked for credit card information, and then enrolled in a free trial for the paid version of the course. After 14 days, they're automatically charged unless they cancel.

If the student clicks *"access course materials"*, they're able to view the videos and take the quizzes for free, but they can't receive coaching support or a verified certificate, and they can't submit their final project for feedback.


### Experiment Design

**Goal of Experiment:**
Test whether the free-trial screener sets clearer initial expectations of course time commitment.

**Mechanics of Experiment:**
The unit of diversion is a **cookie**, although if the student enrolls in the free trial, they are tracked by **user-id** from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.

If the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated **5 or more hours/week**, they would be taken through the checkout process. If they indicated **fewer than 5 hours/week**, a message appeared indicating that courses usually require a greater time commitment for successful completion, suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead. This screenshot shows what the experiment looks like.

### Metric Choice

Invariant metrics are chosen to ensure the internal validity of the experiment, and used when performing *sanity checks* after data collection and before result analysis. Evaluation metrics are chosen to represent the business objectives of the problem at hand. These metrics came from a set list of metrics available.

**Invariant Metrics**

* **# Cookies (dmin=3000):** This metric approximates the number of pageviews. We use this as an initial unit of diversion to ensure an equal split between the control and experiment group. This metric is also independent from the experiment as the user does not see the experiment until they click the button.
* **# Clicks (dmin=240):** This refers to the "start free trial" clicks, and therefore is an independent event that happens before the experiment. Also used to ensure equal split between control and experiment group of users proceeding from course page to experiment page
* **Click-through-probability (dmin=0.01):** Using this as an invariant metric ensures that there are no spurious factors of *button usability*. i.e. the metric normalizes the usuability of the button across different form-factors, and ensures there's no affect from the actual button.

**Evaluation Metrics**
* **Gross Conversion (dmin=0.01):** #UserIDs to enroll in free trial/#UniqueCookies to view the course overview page. A drop in this metric would indicate that screener sets clearer expectations for the students up front, thus reducing the number of frustrated students who left the free trial because they didn't have enough time. However, the overall effect on the business has to be taken in context with another metric.
* **Net Conversion (dmin=0.0075):** #UserIDs to remain past 14 day boundary (and make at least one payment)/#UniqueCookies to click the "Start free trial" button (but not necessarily enroll) This metric (in relation to Gross Conversion) is useful in determining and ensuring the change doesn't significantly reduce the number of students to continue past the free trial, and eventually complete the course. The end goal is to improve user experience, and not deter prospective students in the process. Therefore an increase or constant of this metric, in addition to a drop in Gross Conversion, would be satisficatory for proceeding with the change. 

**Metrics not used**
* **# UserIDs (dmin=50):** The number of users who enroll in a free trial. This is a count metric of total initial enrollments as a user cannot enroll in a course twice. It may be a redudant metric to track as it's value is embedded in the *retention* and *net conversion* metrics.
* **Retention:** Could be used as an evaluation metric for a different business use case, but for the the purposes of this experiment, we're aiming to track conversions


### Measuring Variability (Standard Deviation)

In choosing whether to use an analytical or empirical estimate for the evaluation metrics we check the denominators of our metrics (unit of analysis) and the unit of diversion. If they are the same, we can use an analytical estimate. Both Gross and Net Conversion in this experiment have the same unit of analysis and unit of diversion, number of cookies. This means that it is possible for us to take an analytic measurement, and an empirical estimate of our variance is not necessary.  

The [baseline values](https://docs.google.com/spreadsheets/d/1MYNUtC47Pg8hdoCjOXaHqF-thheGpUshrFA21BAJnNc/edit#gid=0) are used to analytically estimate the standard deviation (SD) of the selection evaluation metrics. A binomial distribution is assumed where SD = sqrt((p\*(1-p)/N)). 

**Gross conversion:**
Number of UserIDs to enroll in free trial/number of UniqueCookies to view the course overview page.


```python
from math import sqrt
def std_dev(p, N):
    std_dev = round(sqrt((p * (1-p)) / N), 4)
    return std_dev
    
```


```python
#sample size is 5000 cookies
samp_size = 5000
p_clickthrough = 0.08
p_enrollgivenclick = 0.20625

# calculate N
pop_size_N = samp_size * p_clickthrough

# calculate STD (binomial)
std_dev(p_enrollgivenclick, pop_size_N)
```




    0.0202



**Net conversion:**
Number of UserIDs to remain past 14 day boundary (and make at least one payment)/ number of UniqueCookies to click the "Start free trial" button (but not necessarily enroll)



```python
#sample size is 5000 cookies
samp_size = 5000
p_clickthrough = 0.08
p_paymentgivenclick = 0.1093125

# calculate N
pop_size_N = samp_size * p_clickthrough

# calculate STD (binomial)
std_dev(p_paymentgivenclick, pop_size_N)

```




    0.0156



Gross Conversion STD: 0.0202  
Net Conversion STD: 0.0156

The evaluation metrics are ratios which both follow a binomial **normal** distribution, and therefore their variability calculated analytically would be comparable with an empirical calculation (i.e. running A/A tests or bootstrap test).


### Sizing
**Number of Samples vs. Power**
The Bonferonni Correction (**α**individual = **α**overall/n) will not be used during the analysis phase. When analyzing multiple metrics, we want to ensure that we correct for a higher probability of false positives resulting from the use of more affective variables. However, we deem the Bonferroni correction too conservative in this experiment, as the metrics are highly correlated. 

The number of samples needed is [calculated here](http://www.evanmiller.org/ab-testing/sample-size.html).

|Metric| Beta| Alpha | Baseline Conversion| dmin|Sample Size per branch| 
|------------------------|
|Gross Conversion | 0.2|0.5|0.20625|0.01 |**25,835** |
|Net Conversion | 0.2|0.5| 0.1093125| 0.0075| **27,413** |

Total # Pageviews needed
= Largest sample size per branch / click through probability / control-experiment split   
= 27,413 / 0.08 / 0.5   
= **685325**  


**Duration vs. Exposure**

The nature of the experiment is low risk; no sensitive data are collected, there's no big difference in the UX imposing inconsistency on the user, and there are no big associated financial costs. For these reasons we kept the exposure to 1, meaning that we'll divert all our pageviews to this experiment. 

The duration is then calculated as a fraction of needed_pageviews/days = unique_cookiesperday
Where:
685325/days = 40000
days = 685325/40000
days = 17.13 or **18**

The experiment needs to be run for 18 days.


### Experiment Analysis

The data used in this study can be found [here](https://docs.google.com/spreadsheets/d/1Mu5u9GrybDdska-ljPXyBjTpdZIUev_6i7t4LRDfXM8/edit#gid=0). 

**Sanity Checks** 
After collecting experiment data, it is important to run sanity check tests to confirm the internal validity of the experiment. By analyzing the invariant metrics, we can confirm that the EXP(experiment) and CONT(control) conditions are comparable.
I compare the number of *cookies* and *clicks* on the start free trail button across the EXP and CONT groups. We assume the split is 50%, i.e. the expected diversion is 0.5.


|Metric| 95% CI| Observed |Pass Sanity|
|------|-------|----------|-----------|
|# Cookies | 0.49882 - 0.5012|0.5006| YES |
|# Clicks | 0.4959 - 0.5041|0.5005| YES|
|P Clickthrough | 0.0812 - 0.0830|0.0822| YES|


For any sanity check that did not pass, explain your best guess as to what went wrong based on the day-by-day data. Do not proceed to the rest of the analysis unless all sanity checks pass.

Calculate the pooled standard error for the control and experiment groups
SEpool = √Ṗpool * (1-Ṗ) * (1/Ncont + 1/Nexp)

**# Cookies**


```python
# pooled Ṗ: Ṗpool = Xcont + Xexp / Ncont + Nexp
# pooled standard error: SEpool = √Ṗpool * (1-Ṗ) * (1/Ncont + 1/Nexp)
from math import sqrt
sum_pageviews_CONT = 345543
sum_pageviews_EXP = 344660

sum_pageviews = (sum_pageviews_CONT + sum_pageviews_EXP)

observed = round(sum_pageviews_CONT/sum_pageviews, 6)
observed = round(345543/690203 +0.5 , 6)
stdpool = sqrt(0.5*0.5/(sum_pageviews))

CIlower = round(-1.96 * stdpool +0.5, 6) 
CIupper = round(1.96 * stdpool +0.5, 6)

pass_test = CIlower < observed < CIupper

print sum_pageviews, stdpool
print "within range =", pass_test
print "CIlower <= observed <= CIupper"
print CIlower, "<=", observed, "<=", CIupper

```

    690203 0.000601840740294
    within range = True
    CIlower <= observed <= CIupper
    0.49882 <= 0.5 <= 0.50118


**# Clicks**


```python
sum_clicks_CONT = 28378
sum_clicks_EXP = 28325
stdpool = sqrt(0.5 * 0.5 /(sum_clicks_CONT + sum_clicks_EXP))
# CIlower = -1.96 *stdpool 
# CIupper = 1.96 *stdpool 
# observed =  sum_clicks_CONT / (sum_clicks_CONT + sum_clicks_EXP) 

CIlower = -1.96 *stdpool + 0.5
CIupper = 1.96 *stdpool + 0.5
observed =  sum_clicks_CONT / (sum_clicks_CONT + sum_clicks_EXP) +0.5

pass_test = CIlower < observed < CIupper

print sum_clicks_CONT + sum_clicks_EXP
print "within range =", pass_test
print "CIlower <= observed <= CIupper"
print CIlower, "<=", observed, "<=", CIupper
```

    56703
    within range = True
    CIlower <= observed <= CIupper
    0.495884495724 <= 0.5 <= 0.504115504276


**Click-through-probability**


```python
# CTP_CONT = sum_clicks_CONT/sum_pageviews_CONT
CTP_CONT = float(28378/345543)
# CTP_EXP = sum_clicks_EXP/sum_pageviews_EXP
CTP_EXP = (28325 / 344660)
print 28378

# pooled Ṗ: Ṗpool = Xcont + Xexp / Ncont + Nexp
# pooled standard error: SEpool = √Ṗpool * (1-Ṗ) * (1/Ncont + 1/Nexp)
ppool = CTP_CONT + CTP_EXP
stdpool = sqrt(ppool * (1-ppool) * (1/sum_pageviews_CONT +1/sum_pageviews_EXP))

CIlower = -1.96 *stdpool 
CIupper = 1.96 *stdpool
observed =  sum_clicks_CONT/ (sum_clicks_EXP+sum_clicks_CONT) 
observed =  sum_clicks_CONT/ (sum_clicks_EXP+sum_clicks_CONT) 

pass_test = CIlower < observed < CIupper

print "within range =", pass_test
print "CIlower <= observed <= CIupper"
print CIlower, "<=", observed, "<=", CIupper
```

    28378
    0.0
    within range = False
    CIlower <= observed <= CIupper
    -0.0 <= 0 <= 0.0


### Result Analysis

After performing the Sanity checks and ensuring the internal validity of the experiment, we can now analyze the results of the evaluation metrics, and determine if our changes to the free trial button are significant to the business.

A metric is statistically significant if the confidence interval does not include 0 (that is, we're confident there was a chance), and it's practically significant if the confidence interval lies outside the practical significance boundary (that is, we're confident there's a change that matters to the business).


**Effect Size Tests**

The effective Size Test was calculated for the evaluation metrics using this [calculator]()

For each of the evaluation metrics, a 95% confidence interval is computed for the difference of the experiment and control group. This means an α = 0.5 and Z = 1.96. We use a sensitivity (1-ß) = 0.8, which is standard.

The dmin for Gross Conversion = +/- 0.01
The dmin for Net Conversion = +/- 0.0075



```python
from math import sqrt
# set dmin numbers
dmin_gross = 0.01
dmin_net = 0.0075

# gross conversion
sum_enroll_CONT = 3785
sum_enroll_EXP = 3423
sum_clicks_enrollpaid_CONT = 17293
sum_clicks_enrollpaid_EXP = 17260

ppool_gross = (sum_enroll_CONT+sum_enroll_EXP)/(sum_clicks_enrollpaid_CONT+sum_clicks_enrollpaid_EXP)
d_gross = (sum_enroll_EXP/sum_clicks_enrollpaid_EXP - sum_enroll_CONT/sum_clicks_enrollpaid_CONT)
stdpool_gross = sqrt(ppool_gross * (1-ppool_gross) * (1/sum_clicks_enrollpaid_CONT + 1/sum_clicks_enrollpaid_EXP))

exp_bound_lower_gross = d_gross - 1.96 *stdpool_gross
exp_bound_upper_gross = d_gross + 1.96 *stdpool_gross
               
# net conversion
sum_paid_CONT = 2033
sum_paid_EXP = 1945

ppool_net = (sum_paid_CONT+sum_paid_EXP)/(sum_clicks_enrollpaid_CONT+sum_clicks_enrollpaid_EXP)
d_net = (sum_paid_EXP/sum_clicks_enrollpaid_EXP - sum_paid_CONT/sum_clicks_enrollpaid_CONT)
stdpool_net = sqrt(ppool_net * (1-ppool_net) * (1/sum_clicks_enrollpaid_CONT + 1/sum_clicks_enrollpaid_EXP))

exp_bound_lower_net = d_net - 1.96 *stdpool_net
exp_bound_upper_net = d_net + 1.96 *stdpool_net
               
print "95% CI of experiment observations for gross conversion: "
print exp_bound_lower_gross,"-", exp_bound_upper_gross
print "95% CI of experiment observations for net conversion: "
print exp_bound_lower_net,"-", exp_bound_upper_net
```

    95% CI of experiment observations for gross conversion: 
    0.0 - 0.0
    95% CI of experiment observations for net conversion: 
    0.0 - 0.0


The Gross Conversion results for the experiment group is statistically significant, the confidence interval doesn't span over zero, and is practically significant.

The Net Conversion results for the experiment group is not statistically significant, the confidence interval spans over zero, and isn't practically significant.

|Metric| 95% CI|Statistical Sig |Practical Sig| 
|------|------|------|-----|
|# Gross Con | -0.0291 - -0.0120| YES | YES |
|# Net Con | -0.0116 - 0.0019|NO| NO|


**Sign Tests** 

I calculated results for the Sign Test using this [online calculator](http://graphpad.com/quickcalcs/binomial1.cfm) I then ran a non-parametric sign test of the day-by-day data to confirm our effect Size Test results. We assume that the baseline probability of people converting is 50%.

Gross conversion: 19 successes, 23 values, p_value = 0.0026 < alpha = 0.05 (statistically significant)

Net conversion: 10 successes, 23 values, p_value = 0.6776 > alpha = 0.05 (not statistically significant)

### Summary
We used an AB test to assess the impact of the course trial process.  The trial process is intended to create a higher satisfaction and conversion to enrollement (perhaps reducing the enrollment rate in general), to screen out users who can't commit to finishing the program, and overall increase the number of students who finish the full program. In sum, the goal is to decrease the the gross conversion, while increasing the net conversion.

Two analysis methods are used to assess the impact, a **Size Effect Test** and a **Sign Test**.

I did not use the [Bonferroni Correction](https://en.wikipedia.org/wiki/Bonferroni_correction).

In order to launch the change, we need both the evaluation metrics to match our expectations, a decrease in gross conversion and a null or positive increase in the net conversion. We are in a situation where the goal is user behaviour, measured temporally with two metrics; both metrics need to be matching what we expect in order to launch, because they are signalling two different points along the chronology of the user's behavior. 

The case where all metrics needing to match the expectations in order to launch is not the same as the case where any metric needs to match the expectations. If this were the case, and the metrics were not highly correlated, the Bonferroni Correction would be appropriate in order to reduce the chance of a Type I error (i.e. If multiple comparisons are done or multiple hypotheses are tested, the chance of a rare event increases, and therefore, the likelihood of incorrectly rejecting a null hypothesis increases.).

Both our sign tests and effect size tests are designed for single metrics, both describing discrete behaviors, so it doesn't make sense to use the correction.


### Recommendation

Although we did see a statistically and practically significant effect on the gross conversion rate by ~2%, this is just an intermediary step and indication of improving the overall experience, (which would be evidenced by an practically significant effect on the **net conversion**). The net conversion difference however was not statistically or fully practically significant in either the Size or Sign tests. However, the net conversion difference does include the negative end of the practical significance boundary, that is, it is possible that net conversion decreased in a way that was practically significant to the business. So it is not advisable to completely dismiss the effectiveness of the change.

From the results we observed, I would recommend re-running the experiment, perhaps slicing by country/other demographic indicator, or changing the wording of the free-trial screener.


### Follow-Up Experiment

Drawing from my own experience as a Udacity student, the most important factor for me was a clear line of sight into the jobs and partner accreditation of the program. This is what differentiated it from other online course options. 

I'd propose a follow-up experiment which hypothesizes that clear job channel and support expectations would increase user retention.

Goal of Experiment: Test whether a career-track screener sets clearer initial expectations of course time commitment and incentivizes people to stay on to the paid program. 

The career-track screener would return something like a list of current open jobs in line with the prospective students' answers to personal interest and goal questions.

The evaluation and invariant metrics would stay the same, and the variable would be a career-track screener (questions TBD), instead of a time-commitment free-trial screener. The unit of diversion would still be a cookie (with the userID tracked after the user enrolled).
