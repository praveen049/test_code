from numpy import math
from sympy import *

def sigmoid(x):
	return 1./(1+math.exp(-x))

vh1 = -6.90675478
vh2 = 0.40546511

q1 = sigmoid(vh2)
q12 = sigmoid (vh1)
q21 = sigmoid (vh1)

# probability of v given h2
pvh2 = sigmoid(vh2) 
#probability of h2
ph2 = 0.5
#probability of h1
ph1 = 0.5
# probability of v given h1
pvh1 = sigmoid(vh1) 
print "pvh1 is", pvh1
#probability of v
pv = (pvh2 * ph2) + (pvh1 * ph1) 
q6 = ((pvh2) * (ph2))/pv

print "q1 is", q1
print "q2 is", q1*0.5 * 0.5
print "q3 is", 0 * (0-q12)
print "q4 is ", 1 * (1-q1)
print "q6 is ", q6

 
