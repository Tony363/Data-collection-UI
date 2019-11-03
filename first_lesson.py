from random import seed
from random import random
import xgboost as xgb
# seed random number generator
seed(1)
# generate random numbers between 0-1
column = []
for _ in range(100):
    row = []
    x1 = random()
    x2 = random()
    row.append(round(x1,2))
    row.append(round(x2,2))
    if x1 + x2 > 1:
        z = 1
        row.append(z)
    else:
        z = 0
        row.append(z)
    print(row)
    column.append(row)
print(column)

