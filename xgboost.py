from random import seed
from random import random
# seed random number generator
seed(1)
# generate random numbers between 0-1

dataset1 = []
dataset2 = []
dataset3 = []
dataset = [dataset1, dataset2,dataset3]

for _ in range(100):
	row = []
    x1 = random()
    x2 = random()
    if x1 + x2 > 1:
        z = 1
        row.append(z)
    else:
        z = 0
        row.append(z)
    
    row.append(x1)
    row.append(x2)
    # print(round(x1,2),round(x2,2),z)
    print(row)

