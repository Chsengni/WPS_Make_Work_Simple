import win32com
import win32com.client

def readWordFiletoWriteOtherFile(path,topath):
    #调用系统Word
    mw=win32com.client.Dispatch("Word.Application")
    doc=mw.Documents.Open(path)
    doc.SaveAs(topath,2)

    doc.Close()
    mw.Quit()

path="D:\\pythonitem\\demo\\Demo7\\1.doc"
topath="D:\\pythonitem\\demo\\Demo7\\2.txt"
readWordFiletoWriteOtherFile(path,topath)
