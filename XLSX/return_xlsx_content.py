from collections import OrderedDict

from pyexcel_xls import get_data


def readxlsAndxlsxile(path):
    dic=OrderedDict()
    xdata=get_data(path)
    for sheet in xdata:
        dic[sheet]=xdata[sheet]
    return dic

path="D:\\pythonitem\\demo\\Demo7\\1.xlsx"
dic1=readxlsAndxlsxile(path)
print(dic1)
