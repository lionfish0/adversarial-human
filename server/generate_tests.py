import pandas as pd
import numpy as np
import json

df = pd.read_csv('training.csv',names=["_","coords","number"])

for picked_start_point in range(20):
    data = []
    init_point = df.iloc[picked_start_point]
    print(init_point['number'],init_point['coords'])

    coords = np.array(json.loads(init_point['coords']))

    print("---")
    print(coords.shape)

    for target in range(10):
        if target==init_point['number']:
            continue
        for coordi in range(len(coords)):
            for axisi in range(2):
                for diri in [-100,-66,-33,33,66,100]:
                    modcoords = coords.copy()/2+100
                    modcoords[coordi,axisi]+=diri
                    data.append([json.dumps(modcoords.tolist()),init_point['number'],target])

                    for coordj in range(len(coords)):
                        for axisj in range(2):
                            for dirj in [-100,-66,-33,33,66,100]:
                                mod2coords = modcoords.copy()
                                mod2coords[coordj,axisj]+=dirj
                                data.append([json.dumps(mod2coords.tolist()),init_point['number'],target])
    data = np.array(data)
    print(data.shape)
    data = data[np.random.choice(len(data),300,replace=False),:]
    pd.DataFrame(data).to_csv('comparison_tests_%d.csv' % picked_start_point,header=['coords','actual','target'])

