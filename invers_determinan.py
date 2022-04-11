import numpy as np

a = np.array(([2,5], [1,3]))

print(a)

# invers matrix
a_inv = np.linalg.inv(a)

print(a_inv)

# determinan
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)

print(det_a)
print(det_a_inv)

# ini bisa menyelesaikan linear