import numpy as np

a = np.floor(np.random.randn(1,6)*10) #floor() buat bulatkan ke bawah #random() data random

print(a)

print("nilai max dari a = ", a.max())
print("posisi nilai max = ", a.argmax())

print("nilai min dari a = ", a.min())
print("posisi nilai min = ", a.argmin())

print("mengurutkan nilai a = ")
print(np.sort(a))
print(np.argsort(a)) #argument / posisi

print("="*100)

# try with matrix
b = np.floor(np.random.randn(2,2)*10) #floor() buat bulatkan ke bawah #random() data random

print(b)

print("nilai max dari b = ", b.max())
print("posisi nilai max = ", b.argmax())

print("nilai min dari b = ", b.min())
print("posisi nilai min = ", b.argmin())

print("mengurutkan nilai b = ")
print(np.sort(b))
print(np.argsort(b)) #argument / posisi

print("="*100)

# with multitype
dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [
    ('hefry', 180),
    ('lukaman', 190),
    ('ilham', 170)
]

c = np.array(data, dtype=dtipe)
print(c)

print(np.sort(c, order='tinggi')) #sesuai tinggi
print(np.sort(c, order='nama')) #sesuai alfabet