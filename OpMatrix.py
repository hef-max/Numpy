import numpy as np

# A = np.array([[1, 1, 1],
#               [1, -2, 1],
#               [-2, 1, 1]])

# x = np.array([[-6, 1, 1],
#               [3, -2, 1],
#               [9, 1, 1]])

# y = np.array([[1, -6, 1],
#               [1, 3, 1],
#               [-2, 9, 1]])

z = np.array([[4,2,0,-1], [8,4,-1, -1],[-1, 0 ,1, 0],[ -6, -3 ,1,1]])



# metode creamer

print(f"jawaban |z| = {np.linalg.inv(z)}")
# n = np.linalg.det(z)
# print(int(n//-16))






# print(f"jawaban |A1| = {int(np.linalg.det(x) / np.linalg.det(A))}")
# print(f"jawaban |A2| = {int(np.linalg.det(y) / np.linalg.det(A))}")
# print(f"jawaban |A3| = {int(np.linalg.det(z) / np.linalg.det(A))}")
























# B = np.array([[2, 0],
#               [0, -3]])

# C = np.array([[1, -2],
#               [3, 1]])
# K = 3
# L = 2




# print(f"1. A+B = B+A:\n {A+B} =\n{B+A}")
# print(f"2. (A+B)+C = A+(B+C):\n {(A+B)+C} =\n {A+(B+C)}")
# print(f"3. A+0 = 0+A = A:\n {A+0} = {0+A} =\n {A}")
# print(f"4. A+(-A) = -A+A = 0:\n {A+(-A)} =\n {-A+A} = 0")
# print(f"5. K(A+B) = KA+KB:\n {np.dot(K, (A+B))} =\n {np.dot(K, A) + np.dot(K, B)}")
# print(f"6. (K+L)A = KA+LA:\n {np.dot((K+L), A)} =\n {np.dot(K, A) + np.dot(L, A)}")
# print(f"7. (KL)A = K(LA):\n {np.dot((K*L), A)} =\n {np.dot(K, (L*A))}")
# print(f"8. 1A = A:\n {np.dot(1, A)} =\n {A}")

# T = (A+B) 
# TAB = [[T[j][i] for j in range(len(T))] for i in range(len(T[0]))]
# TA = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
# TB = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
# print(f"9. {TAB} =\n {TA + TB}")

# print(f"no 7. {np.linalg.det(np.dot(A,B))} =\n {np.dot(np.linalg.det(A), np.linalg.det(B))}")

# A1 = np.array([[2, 1, 0], 
#                [3, 4, 0],
#                [0, 0, 2]])
# print(f"latihan madiri:\n {np.linalg.det(A1)}")





# a = np.array([[1, 2 ],
#              [-3, 0]])
# b = np.array([[0.5, 0],
#              [0, -2],
#              [-1, 3]])
# c = np.array([[4, 1/3, -5],
#              [-3, 0, 1]])
# d = np.array([[0, -2, 1],
#              [-1, 3, 4],
#              [0.5, 0, 1]])
# e = np.array([[2, 0],
#              [0, -3]])
#
# # print("a:", a + b) # not
# # print('b', np.dot(a,b)) # not
# print('c: ', a + e)
# print('d: ', np.dot(a,c))
# # print('e:', np.dot(b, a) + 3 * d)
# print("f: ",np.trace(a))
# print("g: ", np.trace(b))
# print("h: ", np.dot(3, a))
# print("i: ", np.linalg.inv(a))
# print("j: ", np.trace(d))
#
# A = np.array([[1, 2, 3, 4],
#               [8, 7, 6, 5],
#               [9, -1, -2, -3],
#               [-4, -5, -5, -4]
#               ])
# det4x4 = np.linalg.det(A)
# print(f"hasil det4x4 : {det4x4}")
#
# A = np.array([[2, 1],
#                     [4, 3]])
#
# X = np.array([['x1', 'x2'],
#             ['x3', 'x4']])
# print(np.dot(A,X))
#
# # b = np.ones((2,2))
# #
# # print("matrix a:")
# # print(a)
# # print("matrix b:")
# # print(b)
# #
# # # perkalian matrix in aljabar linear
# # c1 = np.dot(a,b)
# # c2 = a.dot(b)
# #
# # print("matrix c1:")
# # print(c1)
# # print("\n")
# # print("matrix c2:")
# # print(c2)
