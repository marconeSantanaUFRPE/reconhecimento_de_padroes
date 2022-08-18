tagsCSV = open("base_flowup/more_used_tags.csv", "r")
tasksCSV = open("base_flowup/bruto2.csv", "r")
tagTasksCSV = open("base_flowup/tag_tasks.csv", "r")
import pandas as pd
import numpy as np



separador = "#"
titleTags = []
for x in tagsCSV.readlines()[1::]:
    id,name,qtdTasks = x.split(",")
    titleTags.append(id)

titleTasks = []
for x in tasksCSV.readlines()[1::]:
    id =  x.split(",")[0]
    titleTasks.append(id)
dd = {}
for x in tagTasksCSV.readlines()[1::]:
    tagId =  x.split(",")[0]
    taskId =  x.split(",")[1].strip()
    dd[taskId,tagId] = 1

dic = {}
for x in titleTasks:
    for y in titleTags:
        try:
            if(dd[x,y]):
                dic[int(x),int(y)] = 1
        except:
            dic[int(x),int(y)] = 0

# print(dic[13992,1])
# df = pd.DataFrame(dic,index=titleTasks,columns=titleTags)
# print(df)

for x in titleTasks:
    linha = ""
    for y in titleTags:
        linha = linha + " " + str(dic[int(x),int(y)])
    print(linha)