import numpy as np

#membuat matrix dengan type data tertentu
a = np.array(([1,2,3], [4,5,6]), dtype= int) #you can change float or other's
print(a)
#membuat array dengan function
def kuadrat(baris, kolom):
    return kolom**2

def jumlah(baris, kolom):
    return (baris + kolom)

# np.fromfunction(fungsi, ukuran, type)
b = np.fromfunction(kuadrat, (1,10), dtype= int)
c = np.fromfunction(jumlah, (4,4), dtype=float)
print(b)
print(c)

#membuat array or matrix dengan menggunakan iterable
iterable = (x*x for x in range(5))
d = np.fromiter(iterable, dtype= int)

# multitype array
dtipe = [('nama', 'S255'), ('tinggi', int)] #'S255' is max_string or max_length

data = [
    ('hefry', 187),
    ('raju', 185),
    ('ary', 170)
]

e = np.array(data, dtype= dtipe)

print(e)