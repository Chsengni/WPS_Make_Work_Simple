import os

import win32com
import win32com.client


def makewordfile(path,name):
    word=win32com.client.Dispatch("Word.Application")
    word.Visible=True
    doc=word.Documents.Add()
    r=doc.Range(0,0)
    r.InsertAfter("亲爱的"+name+"\n")
    r.InsertAfter("        我想你了！\n")
    doc.SaveAs(path)
    doc.Close()
    word.Quit()
names=["张三","李四","王五"]

for name in names:
    path=os.path.join(os.getcwd(),name)
    makewordfile(path,name)
