import numpy as np
import xgboost as xgb
import random

data = np.random.rand(5, 10)  # 5 entities, each contains 10 featusres
label = np.random.randint(2, size=5)  # binary
dtrain = xgb.DMatrix(data, label=label)


# dtest = xgb.DMatrix('test.svm.buffer')

w = np.random.rand(5,1)

param = {'max_depth': 2, 'eta': 1, 'objective': 'binary:logistic'}
param['nthread'] = 4
param['eval_metric'] = 'auc'

evallist = [ (dtrain, 'train')]

num_round = 10

bst = xgb.train(param, dtrain, num_round, evallist)