import csv

def readCsv(path):
    infoList=[]
    with open(path,'r') as f:
        AllfileInfo=csv.reader(f)
        for row in AllfileInfo:
            infoList.append(row)
    return infoList
#只需要导入ReadCsv(本文件)调用readCsv
info=readCsv("1.csv")




