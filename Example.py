import numpy as np
# m = np.array([[1,-1,2],[3,2,0]])
# print(m)
# print("")

# m1 = np.array([[1,2,3]])
# print(np.transpose(m1)) ## Se pasa de vertical a orizontal con el traspose

## Ecuacion 1

# a= np.array([[2,1,-2],[3,0,1],[1,1,-1]])
# print(a)

# print("")
# b = np.array([[-3],[5],[-2]])
# print(np.transpose(b))
# print("")

# x = np.linalg.solve(a,b)
# print(x)

# print(np.allclose(np.dot(a,x),b))

#Ecuacion 2

a = np.array([[2,7,3], [2,8,2],[1,3,1]])
print(a)

b= np.array([[1,1,0]])
b.shape=(3,1) ## tambien se traspone
print(b)

print("")

print(np.linalg.solve(a,b))