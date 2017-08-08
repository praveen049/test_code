from numpy import math
from sympy import *

def sigmoid(x):
	return 1./(1+math.exp(-x))

vh1 = 10
vh2 = -4

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
pvh10 = sigmoid(0) 
print pvh10
#probability of v
pv = (pvh2 * ph2) + (pvh10 * ph1)
print pv
q6 = ((pvh2) * (ph2))/pv

print "q1 is", q1
print "q1 is", pvh2
print "q2 is", q1*0.5 * 0.5
print "q2 is", pvh2*0.5 * 0.5
print "q3 is", 0 * (0-pvh1)
print "q4 is ", 1 * (1-pvh2)
print "q6 is ", q6

 
