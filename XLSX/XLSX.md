# WPS办公操作代码

`读取xlsl文件：`

    from openpyxl.reader.excel import load_workbook

    def readxlsxfile(path):
        file=load_workbook(path)
        sheets=file.sheetnames
        sheet=file.worksheets[0]
        # print(sheet.max_row)
        # print(sheet.max_column)
        # print(sheet.title)

        for lineNum in range(1,sheet.max_row+1):
             linelist = []
             for columnNum in  range(1,sheet.max_column+1):
                value=sheet.cell(row=lineNum,column=columnNum).value
                linelist.append(value)
             print(linelist)


    path="D:\\pythonitem\\demo\\Demo7\\1.xlsx"

    readxlsxfile(path)

***

`写出xlsl文件：`

    from openpyxl.reader.excel import load_workbook

    def readxlsxfile(path):
        file=load_workbook(path)
        sheets=file.sheetnames
        dic={}
        for i in range(len(sheets)):
            sheet=file.worksheets[i]
            sheetinfo=[]

            for lineNum in range(1,sheet.max_row+1):
                linelist = []
                for columnNum in  range(1,sheet.max_column+1):
                    value=sheet.cell(row=lineNum,column=columnNum).value
                    linelist.append(value)

                sheetinfo.append(linelist)

            dic[file.worksheets[i]]=sheetinfo
        return dic



    path="D:\\pythonitem\\demo\\Demo7\\1.xlsx"
    dic1=readxlsxfile(path)
    print(dic1)
***

`简便读取：`

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

