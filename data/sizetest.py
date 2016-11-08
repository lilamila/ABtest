from math import sqrt
# set dmin numbers
dmin_gross = 0.01
dmin_net = 0.0075

# gross conversion
sum_enroll_CONT = 3785
sum_enroll_EXP = 3423
sum_clicks_enrollpaid_CONT = 17293
sum_clicks_enrollpaid_EXP = 17260


ppool_gross = ((sum_enroll_CONT+sum_enroll_EXP) / (sum_clicks_enrollpaid_CONT+sum_clicks_enrollpaid_EXP))
print ppool_gross
# d_gross = (sum_enroll_EXP/sum_clicks_enrollpaid_EXP - sum_enroll_CONT/sum_clicks_enrollpaid_CONT)
d_gross = float(3423/17260)
print d_gross
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