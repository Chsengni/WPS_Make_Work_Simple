import win32com
import win32com.client

def writePPT():
    ppt=win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible=True
    pptFile=ppt.Presentations.Add()
    page1=pptFile.Slides.Add(1,1)
    t1=page1.Shapes[0].TextFrame.TextRange
    t1.Text="CZL"
    t2=page1.Shapes[1].TextFrame.TextRange
    t2.Text="cssac"

    page2=pptFile.Slides.Add(2,1)
    t3= page2.Shapes[0].TextFrame.TextRange
    t3.Text="acsac232323"

writePPT()
