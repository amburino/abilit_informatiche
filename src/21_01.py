import numpy as np
a=np.array([[1,2],[2,2]])
print(a.shape)
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b.shape)
b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum",b,"+",c,"=",b+c)
b +=1
print("incremento b di 1",b)
print("moltiplicazione c*3",c*3)
print("sin(c)",np.sin(c))
v1=np.array([1,2,3]
)
v2=np.array([10,20,30])
print(v1*v2)
print(type(v1*v2))
print(np.dot(v1,v2))
print(type(np.dot(v1,v2)))
######
m1=np.matrix(v1)
m2=np.matrix(v2[:,np.newaxis])
print(m1.shape,m2.shape)
print(m1*m2)
print(np.dot(m1,m2))
