# WPS办公操作代码

`读取.doc文件和.docx文件：`

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
    #doc
    path="D:\\pythonitem\\demo\\Demo7\\1.doc"
	#docx
	#path="D:\\pythonitem\\demo\\Demo7\\1.docx"
    readWordFile(path)
    
调用readWordFile()即可

***

`读取.doc文件和.docx文件和写出文件内容：`

    
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
    