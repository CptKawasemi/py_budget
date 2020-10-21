from tkinter import *
from prettytable import PrettyTable
from Module_Model import *

class BudgetList():
    def __init__(self):
        lf=Toplevel()
        
        lbl=Label(lf)
        lbl.config(font=("Courier",9))
        lbl.pack()
        table=PrettyTable()
        table.field_names=["ItemName","ItemType","Price","Qty","Total"]
        sql="Select ItemName,ItemType,Price,Qty,Qty * Price as 'Total' From budget Order By ItemName;"
        result=Fun_Select(sql)
        
        for row in result:
            col0="%-30s" % row[0] #%-30s% means data to left size of column
            col1="%-30s" % row[1]
            col2="%-30s" % row[2]
            col3="%-30s" % row[3]
            col4="%-30s" % row[4]
            table.add_row([col0,col1,col2,col3,col4])
            
        lbl["text"]=table #table is uploaded onto the label