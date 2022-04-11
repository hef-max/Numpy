import numpy as np

# make vektor
print("part 1 - make vektor")
a = np.array([1,2,3,4,5])
b = np.array([1.2, 2.3, 3.5, 4, 5])
print(a)
print(b)
print(100*"-")

# make vektor with range
print("part 2  - make vektor with range")
c = np.arange(1,10,2) #(lower, upper, interval)
print(c)
print(100*"-")

# make linspace
print("part 3 - make linspace")
d = np.linspace(1,10,4) #sama seperti diatas, namun hanya menampilkan apa yg interval masukan
print(d)
print(100*"-")

# array multidimensi / matrix
print("part 4 - array multidimensi / matrix")
e = np.array([ (1,2,3) , (4,5,6) ])
print(e)
print(100*"-")

# matrix with zero value
print("part 5 - matrix with zero value")
f = np.zeros((5,5))
print(f)
print(100*"-")

# matrix with one value
print("part 6 - matix with one value")
g = np.ones((5,5))
print(g)
print(100*"-")

# matrix identity
print("part 7 - matrix identity")
h1 = np.identity(5)
h2 = np.eye(5)
print(h1)
print("\n")
print(h2)

