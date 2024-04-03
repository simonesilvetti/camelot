import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import pickle
from sklearn.model_selection import train_test_split

data=pd.read_csv('examples/human_integrators/output/integrators_log.csv')

activities = ['Exam', 'hemo_int', 'hemo_inib',
       'sodium_int', 'sodium_inib', 'pot_int',
       'pot_inib', 'recovered',
       'Non responsive']

def zeros(n):
    return [0 for _ in range(n)]

def hot_encode_activity(activity):
    encode = zeros(n_activities+5)
    encode[map_activities[activity[0]]] = 1
    encode[n_activities:] = activity[2:]
    return encode

def hot_encode_trace(trace):
    return [[hot_encode_activity(activity)] for activity in trace]

def trace_to_tensor(trace):
    return torch.tensor(hot_encode_trace(trace), dtype= torch.float32 )


n_activities = len(activities)
map_activities = dict(zip(activities, range(n_activities)))

data.drop('Responsive',axis=1,inplace=True)

traces = [group.values.tolist() for _, group in data.groupby('Case ID')]
train,test=train_test_split(traces,test_size=0.2)

Y_train = [torch.tensor([int(trace[-1][0]=='recovered')],dtype=torch.float) for trace in train]
Y_test = [torch.tensor([int(trace[-1][0]=='recovered')],dtype=torch.float) for trace in test]


reducedTraces_train=[trace[:-len(trace)//2] for trace in train]
transformedTraces_train=[trace_to_tensor(trace) for trace in reducedTraces_train]

reducedTraces_test=[trace[:-len(trace)//2] for trace in test]
transformedTraces_test=[trace_to_tensor(trace) for trace in reducedTraces_test]

for trace in transformedTraces_train:
  nan_mask=torch.isnan(trace)
  trace[nan_mask]=0


for trace in transformedTraces_test:
  nan_mask=torch.isnan(trace)
  trace[nan_mask]=0


with open('examples/human_integrators/dataset/integrators_data_train.pickle', 'wb') as f:
    pickle.dump(transformedTraces_train, f)

with open('examples/human_integrators/dataset/integrators_data_test.pickle', 'wb') as f:
    pickle.dump(transformedTraces_test, f)


with open('examples/human_integrators/dataset/integrators_outputs_train.pickle', 'wb') as f:
    pickle.dump(Y_train, f)

with open('examples/human_integrators/dataset/integrators_outputs_test.pickle', 'wb') as f:
    pickle.dump(Y_test, f)