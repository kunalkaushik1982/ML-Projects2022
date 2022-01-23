#less memory
#Fast
#convenient

from array import array
from unittest import result
import numpy as np
import time
import sys

print('####################Fast#####################')
l=range(1000)
print(sys.getsizeof(5))
print(len(l))
print(sys.getsizeof(5)*len(l))

array=np.arange(1000)
print(array.itemsize)
print(array.size)
print(array.size*array.itemsize)
print('###################Fast######################')

SIZE=1000

l1=range(SIZE)
l2=range(SIZE)

a1=np.arange(SIZE)
a2=np.arange(SIZE)

start=time.time()
result=[(x+y) for x,y in (zip(l1,l2))]
print("Python list took:",(time.time()-start)*1000)



