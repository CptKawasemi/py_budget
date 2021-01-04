#lol

from tkinter import *
import Module_Model
from tkinter import messagebox


class BudgetEntry():

    def getCType(self):
        CT = self.rdoCType.get()
        return CT

    def isNumber(self, value):
        try:
            int(value)
            return True
        except:
            return False

    def btnSave_Click(self):

        if (self.txtItemName.get() == "" or self.getCType() == "" or self.txtPrice.get() == ""):
            messagebox.showwarning("Program Say", "Please Try again after Fill all Record !")
        else:
            bn = Module_Model.Fun_Select("SELECT ItemName FROM budget WHERE ItemName='" + self.txtItemName.get() + "';")
            print(bn)
            if (len(bn) > 0):
                messagebox.showerror("This program say", " This Item Name already exists.")
            else:
                ItemName = self.txtItemName.get()
                print(ItemName)
                ItemType = self.getCType()
                Price = self.txtPrice.get()
                Qty = self.txtQty.get()
                sql = "INSERT INTO budget(ItemName,ItemType,Price,Qty) VALUES ('" + ItemName + "','" + ItemType + "'," + Price + "," + Qty + ");"
                Module_Model.Fun_Execute(sql)
                messagebox.showinfo("Saving", "Successfully Save Record")
                self.txtItemName.delete(0, END)
                self.txtPrice.delete(0, END)
                self.txtQty.delete(0, END)
                self.txtItemName.focus()

    def __init__(self):  # default constructor

        # root = Tk()
        global rdoCType
        self.rdoCType = StringVar()
        lf = Toplevel()
        lf.title("Item Entry")
        lf.geometry("600x400")

        # syntax of Label ( master, option, ... )
        # place the data label and entry in the frame
        Label(lf, text="Enter Item Name : ").grid(row=0, column=0, pady="0.5c", padx="1c")
        self.txtItemName = Entry(lf)  # Entry( master, option, ... )
        self.txtItemName["width"] = 40
        self.txtItemName.grid(row=0, column=1, pady="0.5c")
        self.txtItemName.focus()

        Label(lf, text="Choose Item Type : ").grid(row=1, column=0, pady="0.5c", padx="1c")

        frame = Frame(lf)
        frame.grid(row=1, column=1)

        self.ty = Radiobutton(frame, text="Food", variable=self.rdoCType, value="Food", command=self.getCType)
        self.ty.grid(row=0, column=0, pady="0.5c")
        self.ty.deselect()
        self.ty = Radiobutton(frame, text="Clothing", variable=self.rdoCType, value="Clothing", command=self.getCType)
        self.ty.grid(row=0, column=1, pady="0.5c")
        self.ty.deselect()
        self.ty = Radiobutton(frame, text="Extras", variable=self.rdoCType, value="Extras", command=self.getCType)
        self.ty.grid(row=0, column=2, pady="0.5c")
        self.ty.deselect()

        Label(lf, text="Enter Price : ").grid(row=2, column=0, pady="0.5c", padx="1c")
        # Entry( master, option, ... ) Option = key-value pair
        self.txtPrice = Entry(lf)
        self.txtPrice["width"] = 40
        self.txtPrice.grid(row=2, column=1, pady="0.5c")

        Label(lf, text="Enter Qty : ").grid(row=3, column=0, pady="0.5c", padx="1c")
        # Entry( master, option, ... ) Option = key-value pair
        self.txtQty = Entry(lf)
        self.txtQty["width"] = 40
        self.txtQty.grid(row=3, column=1, pady="0.5c")

        self.btnSave = Button(lf, text="Save")
        self.btnSave.grid(row=4, column=1, pady="0.5c", padx="1c", columnspan=2)
        self.btnSave["command"] = self.btnSave_Click
        self.btnclose = Button(lf, text="Close")
        self.btnclose.grid(row=4, column=0, pady="0.5c", padx="2.5c")
        self.btnclose["command"] = lf.destroy
