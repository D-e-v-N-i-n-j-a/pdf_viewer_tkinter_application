from fileinput import filename
from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

class PDFviewer:
    def __init__(self,root):
        self.root = root
        self.root.title("PDF VIEWER")
        self.root.geometry("630x700+400+100")
        self.root.configure(bg="white")
        def browsePDF():
            fileName = filedialog.askopenfilename(initialdir=os.getcwd(),title="select pdf file",filetypes=(("PDF FILE",".pdf"),("PDF FILE",".PDF"),("ALL FILE",".txt")))
            v1 = pdf.ShowPdf()
            v2 = v1.pdf_view(self.root,pdf_location=open(fileName,"r"),width=77,height=100)
            v2.pack(pady=(0,0))
        
        
        
        
        buttonOpen = Button(self.root,text="SELECT PDF",command=browsePDF,width=40,font=("Arial",15),bd=4).pack()









root = Tk()
obj = PDFviewer(root=root)
root.mainloop()