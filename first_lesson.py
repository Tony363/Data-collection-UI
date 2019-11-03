from random import seed
from random import random
import xgboost as xgb
# seed random number generator
seed(1)
# generate random numbers between 0-1
value_1 = []
value_2 = []
dataset1 = [value_1,value_2]
dataset2 = []


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

for _ in range(10):
    row = []
    x1 = random()
    x2 = random()
    value_1.append(x1)
    value_2.append(x2)
    # if x1 + x2 > 1:
    #     z = 1
    #     dataset3.append(z)
    # else:
    #     z = 0
    #     dataset3.append(z)
print(dataset1)

# x = column[]

