import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
def Fun_Execute(SqlStatement):
    try:
        connection=mysql.connector.connect(host='localhost',database='kmd',user='root',password='kmd')
        if connection.is_connected():
            
            db_Info=connection.get_server_info()
            print("Connected to MySQL Server version",db_Info)
            cursor=connection.cursor()
            cursor.execute(SqlStatement)
            connection.commit()
            connection.close()
    except Error as e:
         print("Error while connecting to MySQL",e)
def Fun_Select(SqlStatement):
    try:
        connection=mysql.connector.connect(host='localhost',database='kmd',user='root',password='kmd')
        if connection.is_connected():
            db_Info=connection.get_server_info()
            print("Connected to MySQL Server version",db_Info)
            cursor=connection.cursor()
            cursor.execute(SqlStatement)
            record=cursor.fetchall()
            return record
            connection.commit()
    except Error as e:
         messagebox.showinfo("Error while connecting to MySQL",e)