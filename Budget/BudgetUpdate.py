from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from Module_Model import*
class BudgetUpdate():
    def click_UpDate(self):
       
        if(self.cbo_itemname.get()=="" or self.rdoCType.get()==0 or self.txtPrice.get()=="" or  self.txtQty.get()==""):
            messagebox.showwarning("Program Say","Please Try again after Fill all Record !")
        else:
            bname=self.cbo_itemname.get();
            btype=self.rdoCType.get();
            cprice=self.txtPrice.get();
            cqty=self.txtQty.get();
            Fun_Execute("UPDATE kmd.budget SET ItemName='"+bname+"',ItemType='"+btype+"',Price='"+cprice+"',Qty='"+cqty+"' WHERE Number="+str(self.ID)+";")
            self.cbo_itemname.delete(0,END)
            self.txtPrice.delete(0,END)
            self.txtQty.delete(0,END)
            messagebox.showinfo("Program Say","Update Process Successful")
            
    def chooseItem(self):
        if(self.rdoCType.get()!="" or self.txtPrice.get()!=""):
            itemname=self.cbo_itemname.get()
            bookdata=Fun_Select("SELECT * FROM budget WHERE ItemName='"+itemname+"';")
            row=bookdata[0]
            self.ID=row[0]
            self.rdoCType.set(row[2])
            self.txtPrice.insert(0,row[3])
            self.txtQty.insert(0,row[4])
            self.uprdo.deselect()
                     
        else:
            self.ClearData()
            
            
        
    def ComfirmUpDate(self):
        if(self.cbo_itemname.get()==""):
            messagebox.showerror("Program Say","Please Choose Item & Try again")
            
        elif(self.cbo_itemname.get() =="" or self.txtPrice.get()!=""):
            messagebox.showerror("Program Say","Please Click Clear & Try again")            
        else:
            self.chooseItem()
                   
    def isNumber(self,value):
        try:
            int(value)
            return True
        except:
            return False

    def ClearData(self):
        self.txtPrice.delete(0,END)
        self.cbo_itemname.delete(0,END)
        self.txtQty.delete(0,END)
        self.RT.deselect()
        self.uprdo.deselect()

    def btnDelete_Click(self):
        item=self.cbo_itemname.get()
        if(item=="" or self.rdoCType.get()=="" or self.txtPrice.get()==""):
            messagebox.showwarning("Program Say","Please Fill All Record")
        else:
            mymessage=messagebox.askyesno("This Program Say","Are You sure You want to Delete!")
            if (mymessage==True):
                Fun_Execute("DELETE FROM budget WHERE ItemName='"+self.cbo_itemname.get()+"';")
                self.ClearData()
                messagebox.showinfo("This Program Say","Delete Done")


    def __init__(self):
        lf = Toplevel()
        self.cid=0;
        self.UpDateSure=IntVar()
        lf.title("Item Update")
        lf.geometry("600x400")
        Label(lf,text="Choose Item Name : ").grid(row=0,column=0)
        #Option Menu
        self.cbo_itemname=ttk.Combobox(lf)
        self.cbo_itemname["value"]=Fun_Select("SELECT ItemName FROM budget")
        self.cbo_itemname.grid(row=0,column=1)
        
        self.uprdo=Radiobutton(lf,text="UpDate",variable=self.UpDateSure,value=1,command=self.ComfirmUpDate)
        self.uprdo.grid(row=0,column=3,pady="0.5c")
        Label(lf,text="Choose Item Type : ").grid(row=1,column=0,pady="0.5c",padx="1c")

        frame=Frame(lf)
        frame.grid(row=1,column=1)

        self.rdoCType=StringVar()
        self.RT=Radiobutton(frame,text="Food", variable=self.rdoCType, value="Food")
        self.RT.grid(row=0,column=0)
        self.RT.deselect()
        self.RT=Radiobutton(frame,text="Clothing", variable=self.rdoCType, value="Clothing")
        self.RT.grid(row=0,column=1)
        self.RT.deselect()
        self.RT=Radiobutton(frame,text="Extras", variable=self.rdoCType, value="Extras")
        self.RT.grid(row=0,column=2)
        self.RT.deselect()
        Label(lf,text="Enter Price : ").grid(row=2,column=0,pady="0.5c",padx="1c")

        self.txtPrice=Entry(lf)
        self.txtPrice["width"]=40
        self.txtPrice.grid(row=2,column=1,pady="0.5c")
        
        Label(lf,text="Enter Qty : ").grid(row=3,column=0,pady="0.5c",padx="1c")
        #Entry( master, option, ... ) Option = key-value pair
        self.txtQty=Entry(lf)
        self.txtQty["width"]=40
        self.txtQty.grid(row=3,column=1,pady="0.5c")

        frame=Frame(lf)                                                  
 
        frame.grid(row=4,column=0,columnspan=3)


        self.btnclose=Button(frame,text="Close")
        self.btnclose.grid(row=0,column=0,padx="1.5c",pady="0.5c")
        self.btnclose["command"]=lf.destroy

        self.btnCancel=Button(frame,text="Clear")
        self.btnCancel.grid(row=0,column=1,padx="1.5c",pady="0.5c")
        self.btnCancel["command"]=self.ClearData
        
        self.btnUpdate=Button(frame,text="Update")
        self.btnUpdate.grid(row=0,column=3,padx="1.5c",pady="0.5c")
        self.btnUpdate["command"]=self.click_UpDate

        self.btnDelete=Button(frame,text="Delete")
        self.btnDelete.grid(row=0,column=2,pady="0.5c")
        self.btnDelete["command"]=self.btnDelete_Click
        
