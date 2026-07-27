import numpy as np
import random
# maps a function called a "sigmoid". Maps any value from 0 to 1, use it to convert numbers to probabilites
def nonlin(x, deriv = False):
    if (deriv == True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# The dataset we are using to predict the outputs of
x = np.array ([  [0,0,1,1],    [0,1,1,0],   [1,0,1,1],    [1,1,1,0]  ])
# output dataset
y = np.array([[0,0,1,1], [1,1,1,1]]).T

#seed random numbers to make calculation
#determinstic (just a good practise)
np.random.seed(1)

#initialises weights randomly with mean 0
syn0 = 2*np.random.random((4,2)) - 1

for iter in range(10000):
    #forward propagation
    l0 = x
    l1 = nonlin(np.dot(l0,syn0))
    # how much did we miss
    l1_error = y - l1
    
    #multiply how much we missed by the slop of the sigmoid at the values in L1
    l1_delta = l1_error * nonlin(l1, True)

    # Update weights
    syn0 += np.dot(l0.T, l1_delta)


print("Output after Training: ")
print(l1)