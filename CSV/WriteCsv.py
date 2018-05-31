import csv

def writeCsv(path,data):
    with open(path,"w") as  f:
       writer= csv.writer(f)
       for rowData in data:
           print("rowData=",rowData)
           writer.writerow(rowData)

# 传入 path 和 要写入的数据即可
writeCsv("2.csv",[[1,2,3],[4,5,6,7],[8,9,10,11,12,13]])
