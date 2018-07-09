import numpy as np

dataset = np.loadtxt("diab.csv", delimiter=",")


X = dataset[:,0:8]
Y = dataset[:,8]
