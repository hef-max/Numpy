import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a)
print(b)
print("\n")

aMat = np.zeros((2,3))
bMat = np.ones((2,3))
print(aMat)
print(bMat)
print("\n")

#stacking matrix, menumpuk matrix
c = np.hstack((a,b)) #hstack [horizontal]
d = np.vstack((a,b)) #vstack [vertikal]
print(c)
print(d)
print("\n")

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat)) #jangan sampai beda ordo
print(cMat)
print(dMat)


#warning jangan sampai beda
#contoh mat(2,3) vs mat(2,2) dengan .vstack()