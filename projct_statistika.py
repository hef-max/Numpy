import numpy as np
import  matplotlib.pyplot as plt
import pandas as pd

data = np.array([60, 55, 65, 70, 75,
                 30, 40, 35, 80, 75,
                 25, 90, 70, 40, 50,
                 90, 85, 75, 65, 45])

data_1 = np.sort(data)
data_2v = pd.Series(data_1)
data_2vi = data_2v.loc[::-1]

print(data_1)
print(data_2vi)

print("data max : ", np.max(data))
print("posisi data max : ", np.argmax(data))
print("data min : ", np.min(data))
print("posisi data min : ", np.argmin(data))
print("banyak nya data 90: ", data[data == 90])
print("banyaknya data 75: ", data[data == 75])

plt.plot(data_1)
plt.show()




# multitype
dtipe = [('jenis_olah', 'S255'), ('frekuensi', int)]
data_3 = [
    ('sepak_bola', 24),
    ('voli', 15),
    ('bulu tangkis', 8),
    ('tenis meja', 3)
]
data_3v = np.array(data_3, dtype=dtipe)

print(np.sort(data_3v, order='frekuensi'))