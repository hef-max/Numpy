import numpy as np

a = np.arange(10)

print(a)

# mengambil nilai
print("element ke-1 dari a adalah",a[0])
print("element ke-7 dari a adalah", a[6])

# slicing [start:stop]
print("element dari 1-6 adalah", a[0:6])
print("element dari 4-stop adalah", a[3:])
print("element dari start-5 adalah", a[:5])

# iterasi
for i in a:
    print('value =', i)
