from random import seed
from random import random
import xgboost as xgb
import numpy as np
import operator

seed(1)
# value_1 = []
# value_2 = []
# X = np.array([value_1,value_2])

X = []
Y = []
 
for _ in range(10):
    row = []
    x1 = random()
    x2 = random()
    row.append(x1)
    row.append(x2)
    X.append(row)

    if x1 + x2 > 1:
         z = 1
         Y.append(z)
    else:
         z = 0
         Y.append(z)
X_sorted = sorted(X, key=operator.itemgetter(0))
print(X_sorted)
print(Y)



# column = []
# for _ in range(10):
#     row = []
#     x1 = random()
#     x2 = random()
#     row.append(round(x1,2))
#     row.append(round(x2,2))
#     if x1 + x2 > 1:
#         z = 1
#         row.append(z)
#     else:
#         z = 0
#         row.append(z)
#     print(row)
#     column.append(row)
# print(column)
