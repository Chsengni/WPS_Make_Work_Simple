# WPS办公操作代码

`读取PDF：`

    import importlib
    import sys
    
    importlib.reload(sys)
    
    from pdfminer.pdfparser import PDFParser,PDFDocument
    from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
    from pdfminer.converter import PDFPageAggregator
    from pdfminer.layout import LTTextBoxHorizontal,LAParams
    from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
    def readPDF(path,topath):
       f=open(path,'rb')
       parser=PDFParser(f)
       pdfFile=PDFDocument()
       parser.set_document(pdfFile)
       pdfFile.set_parser(parser)
       pdfFile.initialize()
    
       if not pdfFile.is_extractable:
       raise  PDFTextExtractionNotAllowed
       else:
       #解析数据
       manager=PDFResourceManager()
       #创建一个PDF对象
       laparams=LAParams()
       device=PDFPageAggregator(manager,laparams=laparams)
       #解析器对象
       interpreter=PDFPageInterpreter(manager,device)
       for page in pdfFile.get_pages():
       interpreter.process_page(page)
       layout=device.get_result()
       for x in layout:
       if(isinstance(x,LTTextBoxHorizontal)):
       with open(topath,'a') as f:
      str=x.get_text()
      print(str)
      f.write(str+'\n')
      f.close()
    
    
    
    
    readPDF("C:\\Users\\xiaolin\\Desktop\\Python之tkinter中文教程.pdf","1.txt")

所以直接导入ReadPdf即可调用readPDF方法
