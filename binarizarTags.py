tagsCSV = open("base_flowup/more_used_tags.csv", "r")
tasksCSV = open("base_flowup/base_horas_fast.csv", "r")
tagTasksCSV = open("base_flowup/tag_tasks.csv", "r")
import pandas as pd
import numpy as np

def binarizacao ():

    arquivo = open("result.csv", "w")

    string = ""
    separador = "#"
    titleTags = []
    for x in tagsCSV.readlines()[1::]:
        id,name,qtdTasks = x.split(",")
        titleTags.append(id)
        string = string+","+name
    arquivo.write(string+"\n")
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

    for x in titleTasks:
        linha = ""
        for y in titleTags:
            linha = linha + "," + str(dic[int(x),int(y)])
        arquivo.write(linha+"\n")

def mergearDados ():

    b_tags = open("csv/tags_binarizadas.csv", "r").readlines()
    new_base = open("csv/dataframe.csv", "w")
    y = 0
    a = tasksCSV.readlines()
    for x in range(len(a)):
        linha = a[x].strip() + b_tags[x].strip()
        new_base.write(linha+"\n")


#binarizacao()
mergearDados()