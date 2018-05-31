# 办公操作代码
    import csv
    def readCsv(path):
       infoList=[]
      with open(path,'r') as f:
             AllfileInfo=csv.reader(f)
             for row in AllfileInfo:
                infoList.append(row)
        return infoList
    info=readCsv("1.csv")
    print(info)
