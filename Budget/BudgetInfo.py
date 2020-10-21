from tkinter import*
from BudgetEntry import*
from BudgetList import *
from BudgetUpdate import *


class BudgetInfo():
    
    def UD_Click(self):
        BudgetUpdate()
    def Listing_Click(self):
        BudgetList()
    def Entry_Click(self):
        BudgetEntry()
    def __init__(self):
        self.ShowForm()
        
   
    def Exit_Click(self):
        form.destroy()
        exit()

    def ShowForm(self):
        
        for w in form.children.values():#to check the previous display on form
            w.destroy()
        
        menu=Menu()
        form.configure(menu=menu) #to upload menu on form, (menu=obj) is default

        filemenu=Menu(tearoff=0) #0 means filemenu is empty, 1 means "-----"
        #is added to filemenu
        menu.add_cascade(menu=filemenu,label="File")

        #filemenu1=Menu(tearoff=0)
        #menu.add_cascade(menu=filemenu1,label="Edit")
         
        filemenu.add_command(label="Entry",command=self.Entry_Click)
        filemenu.add_command(label="Update/Delete",command=self.UD_Click)
        filemenu.add_command(label="Listing",command=self.Listing_Click)

        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=self.Exit_Click)

form=Tk()
form.title("Personal Budget Program")

width=form.winfo_screenwidth()
height=form.winfo_screenheight()
form.geometry(str(width)+'x'+str(height))

#form.geometry('500x500')


Form=BudgetInfo()
form.mainloop()

