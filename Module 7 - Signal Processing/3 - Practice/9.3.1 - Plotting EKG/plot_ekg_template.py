import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

data = np.loadtxt(path, delimiter=',', skiprows=2)

# save each vector as own variable
vector1 = data[:,0]

vector2 = data[:,1]



print(vector1, vector2)

# use matplot lib to generate a single
plt.plot(vector1, vector2)
plt.title('EKG Data')
plt.xlabel('Time')
plt.ylabel('V1')
plt.xlim(0, 5)
plt.show()

## office hours