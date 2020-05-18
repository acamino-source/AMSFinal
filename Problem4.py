import numpy as np
import scipy.linalg as lalg
import numpy.matlib as npm
import matplotlib.pyplot as plt

eps = 1e-4 # Precision of eigenvalue

# creating a numpy 2^12x2^12 array A with normally distributed random numbers g_(i,j)~N(0,1) as it's elements
# this means a normal distribution with mu = 0 and standard deviation of 1.0
A = np.random.normal(0,1,(2**12, 2**12))
#print(A)

# calculating the dominant eigenvalues and eigenvectors using scipy module .eig
# Using numpy's "linalg" library and the eig() function gives us the eigenvalues and eigenvectors, which I then converted the eigenvalues from a numpy array into a list in order to use the "index" here to find the position of the largest eigenvalue and thus pick the corresponding column from the eigenvector array
eigenvalues, eigenvectors = lalg.eig(A)
#print(eigenvalues)
#print(eigenvectors)
largest_eigenvalue = max(eigenvalues)
print("The largest eigenvalues is", largest_eigenvalue)
maxcol = list(eigenvalues).index(max(eigenvalues))
largest_eigenvector = eigenvectors[:,maxcol]
print("The corresponding largest eigenvector is", largest_eigenvector)

#make a histogram of the matrix elements
ax = plt.hist(A)
bins_list = [-1,-0.5,-0.25,0.25,0.5,1]
ax = plt.hist(A, bins = bins_list)
plt.show()

op = "Charactristic equation of A is : (x-{})*(x-{})*(x-{})"
#print(op.format(eigenvalues[0],eigenvalues[1],eigenvalues[2]))


