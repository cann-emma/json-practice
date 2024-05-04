import json
with open('schacon.repos.json', 'r') as file:
    data = json.load(file)


info= [ ]
for i in data:
    myselect= (i['name'], i['html_url'], i['updated_at'], i['visibility'])
    info.append(myselect)
    #print(info)

with open('schacon.csv', 'w') as f:
    json.dump(info[:5], f)

with open('schacon.csv', 'r') as myfile:
    mydat= json.load(myfile)

    for i in mydat:
        print(i)

