# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#######bst.predict()
from random import seed
from random import random
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
import numpy as np
import xgboost as xgb
import operator

# f=open("dump.raw.txt","w+")
# g=open("featmap.txt","w+")
# A=[[random(),random()] for i in range(10)]

# seed(1)

X=[]
Y=[]

for i in range(100):
    row = []
    x1 = random()
    x2 = random()
    # px1=str(round(x1,3))
    # px2=str(round(x2,3))
    row.append(x1)
    row.append(x2)
    X.append(row)
    #print(float(px1), float(px2))
    if x1 + x2 >= 1:  
        z = 1
        Y.append(z)    
    else: 
        z = 0
        Y.append(z)


print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

dtrain = xgb.DMatrix(X[0:70],label=Y[0:70])
dtest = xgb.DMatrix(X[71:100],label=Y[71:100])

dtrain_svm = xgb.DMatrix('dtrain.svm')
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

bst.save_model('0001.model')
bst.dump_model('dump.raw.txt')


bst_svm = xgb.train(param, dtrain_svm, num_round)
preds_ = bst.predict(dtest_svm)
best_preds_svm = [np.argmax(line) for line in preds_]

bst_svm.save_model('0002.model')
bst_svm.dump_model('dump_svm.raw.txt','featmap.txt')

#A saved model can be loaded as follows:
bst = xgb.Booster({'nthread': 4})  # init model
bst.load_model('model.bin')  # load data
# f.close
# g.close

# save the models for later
# joblib.dump(bst, 'bst_model.pk1', compress=True)
# joblib.dump(bst_svm, 'bst_svm_model.pk1', compress=True)

print("Numpy array precision:{}".format(precision_score(Y_test, best_preds )))
    
print("Svm file precision:{}".format(precision_score(Y_test, best_preds_svm)) )

# bst = xgb.Booster({'nthread': 4})  # init model
# bst.load_model('model.bin')  # load data



