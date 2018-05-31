import win32com
import win32com.client

def readWordFile(path):
    #调用系统Word
    mw=win32com.client.Dispatch("Word.Application")
    doc=mw.Documents.Open(path)
    for par in doc.Paragraphs:
        line=par.Range.Text
        print(line)
    doc.Close()
    mw.Quit()
path="D:\\pythonitem\\demo\\Demo7\\1.doc"
#path="D:\\pythonitem\\demo\\Demo7\\1.docx"
readWordFile(path)
