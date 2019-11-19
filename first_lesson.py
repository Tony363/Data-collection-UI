# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#######bst.predict()
from random import seed
from random import random
import numpy as np
import xgboost as xgb
import operator

f=open("dump.raw.txt","w+")
g=open("featmap.txt","w+")
# A=[[random(),random()] for i in range(10)]

seed(1)

X=[]
Y=[]

for _ in range(10):
    row=[]
    x1 = random()
    x2 = random()
    px1=str(round(x1,3))
    px2=str(round(x2,3))
    row.append(x1)
    row.append(x2)
    X.append(row)
    #print(float(px1), float(px2))
    if x1+x2>1:  
        z=1
        Y.append(z)    
    else: 
        z=0
        Y.append(z)


print(X)
print(Y)


#need to get list first item and sort it
X_sorted = sorted(X, key=operator.itemgetter(0))
print(X_sorted)

#remove a value from the list

dtrain=xgb.DMatrix(X[0:70],label=Y[0:70])
dtest=xgb.DMatrix(X[71:100],label=Y[71:100])
dtest_svm = xgb.DMatrix('dtest.svm')

param = {
        'max_depth': 3, 
        'eta': 2, 
        'objective': 'binary:logistic'
        }
param['nthread'] = 4
param['eval_metric'] = 'auc'
evallist = [(dtest, 'eval'), (dtrain, 'train')]
num_round = 5

bst = xgb.train(param, dtrain, num_round, evallist)
preds = bst.predict(dtest)
best_preds = np.asarray([np.argmax(line) for line in preds])

bst_svm = xgb.train(param, dtrain_svm, num_round)
preds_ = bst.predict(dtest_svm)

bst.save_model('0001.model')
#The model and its feature map can also be dumped to a text file.

# dump model
bst.dump_model('dump.raw.txt')
# dump model with feature map
bst.dump_model('dump.raw.txt', 'featmap.txt')
#A saved model can be loaded as follows:
f.close
g.close

# bst = xgb.Booster({'nthread': 4})  # init model
bst.load_model('model.bin')  # load data



