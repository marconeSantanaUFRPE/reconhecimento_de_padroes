import pandas as pd
import numpy as np

def binarizacao ():

    arquivo = open("csv/tags_binarizadas.csv", "w")

    string = ""
    tagsIds = []
    tagsCSV = open("base_flowup/more_used_tags.csv", "r")

    for x in tagsCSV.readlines()[1::]:
        id,name,qtdTasks = x.split(",")
        tagsIds.append(id)
        string = string+","+name
    arquivo.write(string+"\n")
    tasksIds = []
    tasksComExp = open("base_flowup/base_horas_fast_exp.csv", "r")
    for x in tasksComExp.readlines()[1::]:
        id =  x.split(",")[0]
        tasksIds.append(id)
    dd = {}
    #fazer a query
    tagTasksCSV = open("base_flowup/tag_tasks.csv", "r")

    for x in tagTasksCSV.readlines()[1::]:
        tagId =  x.split(",")[0]
        taskId =  x.split(",")[1].strip()
        if(taskId in tasksIds):
            if(tagId in tagsIds[0:len(tagsIds)-1]):
                dd[taskId,tagId] = 1
            else:
                dd[taskId,'0'] = 1
    print(dd)
    dic = {}
    print(tagsIds)
    for x in tasksIds:
        for y in tagsIds:
            try:
                if(dd[x,y]):
                    dic[int(x),int(y)] = 1
            except:
                dic[int(x),int(y)] = 0

    for x in tasksIds:
        linha = ""
        for y in tagsIds:
            linha = linha + "," + str(dic[int(x),int(y)])
        arquivo.write(linha+"\n")

def mergearDados ():
    tasksCSV = open("base_flowup/base_horas_fast_exp.csv", "r")

    b_tags = open("csv/tags_binarizadas.csv", "r").readlines()
    new_base = open("csv/dataframe.csv", "w")
    a = tasksCSV.readlines()
    for x in range(len(a)):
        linha = a[x].strip() + b_tags[x].strip()
        new_base.write(linha+"\n")


def experiencia():
    dic = {}
    tasksSemExp = open("base_flowup/base_horas_fast_exp.csv", "w")
    usersExp = open("base_flowup/experiencia.csv", "r")
    for x in usersExp.readlines()[1::]:
        id,TotalTasks,TasksAtrasada,TasksNaoAtrasadas = x.split(",")
        nota = 0
        nota2 = 0 
        nota3 = 0
        TotalTasks = int(TotalTasks)
        TasksNaoAtrasadas = int(TasksNaoAtrasadas)
        TasksAtrasada = int(TasksAtrasada)
        if(TotalTasks==0):
            propTasks = 0
            propAtrasadaTasks = 1
        else:
            propTasks = TasksNaoAtrasadas/TotalTasks
            propAtrasadaTasks = TasksAtrasada/TotalTasks
        if(TotalTasks> 1000 and TasksNaoAtrasadas):
            nota = 10
        elif(TotalTasks > 800):
            nota = 8
        elif(TotalTasks > 600):
            nota = 6
        elif(TotalTasks > 400):
            nota = 4
        elif(TotalTasks > 200):
            nota = 2
        else:
            nota = 1
        if(propTasks > 0.85):
            nota2 = 10
        elif(propTasks >  0.65):
            nota2 = 8
        elif(propTasks >  0.45):
            nota2 = 6
        elif(propTasks >  0.20):
            nota2 = 4
        elif(propTasks >  0.10):
            nota2 = 2
        else:
            nota2 = 1

        if(propAtrasadaTasks <= 0.18):
            nota3 = 10
        elif(propAtrasadaTasks >  0.18 and propAtrasadaTasks <=  0.30):
            nota3 = 8
        elif(propAtrasadaTasks >  0.30 and propAtrasadaTasks <=  0.45):
            nota3 = 6
        elif(propAtrasadaTasks >  0.45 and propAtrasadaTasks <=  0.60):
            nota3 = 4
        elif(propAtrasadaTasks >  0.60 and propAtrasadaTasks <  0.80):
            nota3 = 2
        else:
            nota3 = 1

        dic[int(id)] = (nota+nota2+nota3) / 3
    dic[0] =  0
    tasksSemExp.write("id" + "," + "intervalo" + "," + "estimativa" +","+ "responsavel"+","+"totalsub"+","+"urgente"+"," + "alta" +","+"tempoGasto"+","+"classe"+"\n")
    tasksCSV = open("base_flowup/base_horas_fast.csv", "r")

    for x in tasksCSV.readlines()[1::]:
         id,intervalo,estimativa,responsavel,totalsub,urgente,alta,tempoGasto,classe =  x.split(",")
         nota = dic[int(responsavel)]
         linha = (id + "," + intervalo + "," + estimativa +","+ str(nota) +","+totalsub+","+urgente+"," + alta +","+tempoGasto+","+classe)
         tasksSemExp.write(linha)


if __name__ == "__main__":
    experiencia()
    binarizacao()
    mergearDados()