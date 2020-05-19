import random
import math
import matplotlib.pyplot as plt

N=10000
Δx=1/N
y_init=1
x_init=0

y=[]
x=[]
y=y0
x=x0
for i in range(N):
    y__=y/x
    y+=Δx*y__(x,y) #where y' is equal to y__
    x+=Δx
    x_values.append(x)
    y_values.append(y)


#Graph 
plt.plot(x_values,y_values)
plt.show()
