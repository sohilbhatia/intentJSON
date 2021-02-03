import uuid
import json
import pandas as pd
import os
import pathlib

df = pd.read_excel('TBIntents.xlsx')
i = 0

rows = (len(df.index))

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        
for i in range(rows):
    
    myArray = df.iloc[i].to_numpy()
    res = []
    for val in myArray:
        if pd.isnull(val):
            pass
        else:
            res.append(val)
    print(res)


    uuid.uuid4()
    genid = str(uuid.uuid4())


    false = False
    null = None

    with open('starter.json') as f:
        data = json.load(f)
        
    if (len(res) > 3):
        next = data["userSays"]
        next.append((take))

        next[1]["data"][0]["text"] = (next[0]["data"][0]["text"]).replace("phrase1", res[2])
        intentid = str(uuid.uuid4())
        next[1]["id"] = (next[0]["id"]).replace('intentID', intentid)
        
        if (len(res) > 4):
            next.append((take2))
            next[2]["data"][0]["text"] = (next[0]["data"][0]["text"]).replace("phrase1", res[3])

    take =  {"isTemplate": false, "data": [{"text": "phrase2", "userDefined": false}], "count": 0, "id": "c63f267c-dfce-45c6-8ebe-c8b1460a9cb1", "updated": null}
    take2 = {"isTemplate": false, "data": [{"text": "phrase3", "userDefined": false}], "count": 0,"id": "c63f267c-dfce-45c6-8ebe-c8b1460a9cb1", "updated": null}
    
    data["id"] = (data["id"]).replace("id_here", genid)
    data["name"] = (data["name"]).replace("comp_name", res[0])
    
    item = data["userSays"]
    item[0]["data"][0]["text"] = (item[0]["data"][0]["text"]).replace('phrase1', res[1])
    intentid = str(uuid.uuid4())
    item[0]["id"] = (item[0]["id"]).replace('intentID', intentid)

    capture = data["responses"]

    capture[0]["messages"][0]["speech"] = res[len(res)-1]
    writeToJSONFile('./',('intent' + str(i)),data)
