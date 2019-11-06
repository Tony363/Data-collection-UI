from random import seed
from random import random
from sklearn.model_selection import train_test_split
#import xgboost as xgb
import numpy as np
import operator

seed(1)
# value_1 = []
# value_2 = []
# X = np.array([value_1,value_2])
# x, y = np.arange(10).reshape((5, 2)), range(5) #np.random.randint(5, size=(2, 4))
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
 
X = [[random(),random()] for i in range(10)]
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

del X[5]
X_sorted = sorted(X, key=operator.itemgetter(0))

print(len(X_sorted[0]))
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
