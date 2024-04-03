import pandas as pd
import torch
import pickle
from sklearn.model_selection import train_test_split


data=pd.read_csv('examples/human_integrators/output/integrators_log.csv')

activities = ['hemo_int', 'hemo_inib',
       'sodium_int', 'sodium_inib', 'pot_int',
       'pot_inib', 'recovered',
       'Non responsive']

def zeros(n):
    return [0 for _ in range(n)]


def hot_encode_activity(activity):
    encode=activity[:3]
    encode.extend(zeros(n_activities))
    encode[map_activities[activity[3]]] = 1
    encode.append(activity[-1])
    return encode

def hot_encode_trace(trace):
    return [hot_encode_activity(activity) for activity in trace]

def trace_to_tensor(trace):
    return torch.tensor(hot_encode_trace(trace), dtype= torch.float32 )

n_activities = len(activities)
map_activities = dict(zip(activities, [i+3 for i in range(n_activities)]))

data.drop('Responsive',axis=1,inplace=True)

traces = [group.values.tolist() for _, group in data.groupby('Case ID')]

exam_therapy=[]

for trace in traces:
    case=[]
    for i in range(0,len(trace)-1,2):
        moment=trace[i][2:5]
        moment.append(trace[i+1][0])
        moment.append(trace[i+1][5])
        case.append(moment)
    exam_therapy.append(case)

train,test=train_test_split(exam_therapy,test_size=0.2)

transformedTraces_train=[trace_to_tensor(trace) for trace in train]

transformedTraces_test=[trace_to_tensor(trace) for trace in test]

for trace in transformedTraces_train:
  nan_mask=torch.isnan(trace)
  trace[nan_mask]=0


for trace in transformedTraces_test:
  nan_mask=torch.isnan(trace)
  trace[nan_mask]=0

with open('examples/human_integrators/dataset_next_state/integrators_next_state_train.pickle', 'wb') as f:
    pickle.dump(transformedTraces_train, f)

with open('examples/human_integrators/dataset_next_state/integrators_next_state_test.pickle', 'wb') as f:
    pickle.dump(transformedTraces_test, f)
