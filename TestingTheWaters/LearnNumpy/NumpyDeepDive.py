# a=[1,2,3,4,5]
# b=[10,11,12,13,14]
# print(a+b)

# result=[]

# for i,j in zip(a,b):
#     result.append(i+j)

# print(result)

import numpy as np
a=np.array([1,2,3,4])
print(type(a))
print(a.dtype)

print('##################')

f=np.array([1.2,3.5,5.7,7.9])
print(type(f))
print(f.dtype)
print(a[0])
print(a.ndim)
print(a.shape)
print(f.shape)
print(f.ndim)