#import numpy as np
#creating an array using np.array()method
#arr = np.array([10, 20, 30, 40, 50])
#print(arr)

#a = np.array([[1,2], [3,4], [5,6], [7,8], [9,10]])
#print(a)

#min dimension
#a = np.array([1,2,3,4,5], ndmin= 0)
#print(a)

#datatype parameter
#a = np.array([1, 2, 3], dtype = int)
#print(a)

"""
import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Modified array is:')
for x in np.nditer(a):
    print(x)
"""
"""
import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Transpose of the original array is:')
b = a.T
print(b)
print('\n')
print ('Modified array is:')
for x in np.nditer(b):
    print(x)
"""

import pandas as pd
import numpy as np

df =pd.DataFrame(np.random.randn(4,3),columns =['col1', 'col2', 'col3'])
for row_index, row in df.iterrows():
    print(row_index, row)