#perkalian vektor

import numpy as np

# perkalian dot
a = np.array([1,3])  # bisa juga x,y,z
b = np.array([2,1])

hasil = np.dot(a,b)

print(hasil)

# perkalian cross
c = np.array([1,2,0])
d = np.array([2,1,0])

hasil1 = np.cross(c,d) # var c ngcross ke d [muter ke bawah]
hasil2 = np.cross(d,c) # vara d ngcross ke c [muter ke atas]

print(hasil1)
print(hasil2)