import pandas as pd
import numpy as np
import json

df = pd.read_csv('training.csv')

picked_start_point = 0
target = 3
init_point = df.iloc[picked_start_point]
print(init_point['coords'])

coords = np.array(json.loads(init_point['coords']))
data = []
for coordi in range(len(coords)):
    for axisi in range(2):
        modcoords = coords.copy()/2+200
        modcoords[coordi,axisi]+=200
        for coordj in range(len(coords)):
            for axisj in range(2):
                mod2coords = modcoords.copy()
                mod2coords[coordj,axisj]+=200
                #mod2coords[mod2coords>480] = 480 #to do :reinstate
                #mod2coords[mod2coords<20] = 20
                data.append([json.dumps(mod2coords.tolist()),init_point['number'],target])
                mod2coords[coordj,axisj]-=400 #subtract 200 twice
                #mod2coords[mod2coords>480] = 480 #to do :reinstate
                #mod2coords[mod2coords<20] = 20
                data.append([json.dumps(mod2coords.tolist()),init_point['number'],target])                
data = np.array(data)
pd.DataFrame(data).to_csv('comparison_tests.csv',header=['coords','actual','target'])

