from numpy import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

Wxh= 0.5
Whh= -1.0
Why= -0.7
hbias= -0.1

xt0 = 9
xt1 = 4
xt2 = -2

zt0 = Wxh * xt0 + hbias
ht0 = sigmoid(zt0)
yt0 = Why*ht0


zt1 = (Wxh*xt1)+(Whh * ht0)+hbias
ht1 = sigmoid(zt1)
yt1 = (Why*ht1)

zt2 = (Wxh * xt2)+(Whh * ht1)+hbias
ht2 = sigmoid(zt2)
yt2 = (Why*ht2)

print ('h vales ht0:%f ht1:%f  ht2:%f' %(ht0,ht1,ht2))
print ("sigmoid vales zt0:%f zt1:%f  zt2:%f" %(zt0,zt1,zt2))
print ("outpyt vales y0:%f y1:%f  y2:%f" %(yt0,yt1,yt2))

