from numpy import math
from sympy import *

def sigmoid(x):
	return 1./(1+math.exp(-x))

Wxh= 0.5
Whh= -1.0
Why= -0.7
hbias= -0.1
ybias=0.0

x0 =9
x1 = 4
x2 = -2
'''
Wxh= -0.1
Whh= 0.5
Why= 0.25
hbias= 0.4
ybias=0.0

x0 = 18
x1 = 9
x2 = -8
'''
z0 = (Wxh* x0) + hbias
h0 = sigmoid(z0)
y0 = (Why*h0)
t0 = 0.1
E0 = 0.5*((t0 - y0)**2)

z1 = (Wxh*x1) + (Whh * h0) + hbias + 0.5
h1 = sigmoid(z1)
y1 = (Why* h1)
t1 = -0.1
E1 = 0.5*((t1 - y1)**2)

z2 = (Wxh * x2) + (Whh * h1) + hbias
h2 = sigmoid(z2)
y2 = (Why*h2)
t2 = -0.2
E2 = 0.5*((t2 - y2)**2)

Err = E0 + E1 + E2

y = (t2-y2) * Why * sigmoid(z2) * sigmoid (1-z2) 

print "z0 is", z0
print "h0 is", h0
print "y0 is", y0
print "E0 is", E0

print "z1 is", z1
print "h1 is", h1
print "y1 is", y1
print "E1 is", E1

print "z2 is", z2
print "h2 is", h2
print "y2 is", y2
print "E2 is", E2

print "\nError is", Err
