from collections import OrderedDict

from pyexcel_xls import save_data


def makeexcelfile(path,data):
    dic=OrderedDict()
    for sheetName,sheetValue in data.items():
        d={}
        d[sheetName]=sheetValue
        dic.update(d)
    save_data(path,dic)

path="D:\\pythonitem\\demo\\Demo7\\2.xls"
makeexcelfile(path,{"表1":[[1,2,3],[4,5,6],[7,8,9]],"表2":[[11,22,33],[44,55,66],[77,88,99]]})
