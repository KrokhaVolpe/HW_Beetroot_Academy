import sqlite3
import tkinter as tk
from tkinter import ttk
import pandas as pd

def connect():
    pass
    

# Create the Tkinter GUI
root = tk.Tk()
root.title("Payments")
root.geometry("500x500")

# #Create a listbox to display the data
# listbox = tk.Listbox(root)
# listbox.grid(row=15, column=0, padx=5, columnspan=6)

# #Creating a treeview 1
# tree = ttk.Treeview(root, columns=("AdmNo", "Name", "Class"))
# tree.heading("#0", text="AdmNO")
# tree.heading("#1", text="Name")
# tree.heading("#2", text="Class")

# tree.column("#0", minwidth=15, width=50, stretch=tk.NO)
# tree.column("#1", minwidth=15, width=50, stretch=tk.YES)
# tree.column("#2", minwidth=15, width=50, stretch=tk.NO)
# tree.grid(row=8)

# #creating a frame
# frame = tk.LabelFrame(root, width=50)
# scrollbar = tk.Scrollbar(frame)

# #creating treeview2
# style = ttk.Style()  #adding style
# style.theme_use('default')

# #configure treeview colours
# style.configure("Treeview",
#     background="#D3D3D3",
#     foreground="black",
#     rowheight=25,
#     fieldbackground="#D3D3D3")
# style.map('Treeview',
#    background=[('selected', "#347083")])

# # creating treeview frame
# tree_frame = frame(root)
# tree_frame.grid()

# #creating tree scrollbar
# tree_scroll = scrollbar(tree_frame)
# tree_scroll.pack(side="right", fill="y")

# #creating our treeview
# my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
# my_tree.grid()

# #configure scrollbar
# tree_scroll.config(command=my_tree.yview)

# #define columns
# my_tree['columns'] = ("AdmNo", "Name", "Class")

# #Format columns
# my_tree.column("#0", width=0)
# my_tree.column("AdmNo", anchor="center", width=50)
# my_tree.column("Name", anchor="w", width=140)
# my_tree.column("Class", anchor="center", width=0)

# #column headings
# my_tree.heading("#0", text="", anchor="w")
# my_tree.heading("AdmNo", text="AdmNo", anchor="center")
# my_tree.heading("Name", text="Name", anchor="w")
# my_tree.heading("Class", text="Class", anchor="w")

# Create a Treeview widget to display the data
tree = ttk.Treeview(root, columns=("AdmNo", "Name", "Class"))
tree.heading("#0", text="AdmNo")
tree.heading("#1", text="Name")
tree.heading("#2", text="Class")
tree.column("#0", minwidth=0, width=100, stretch=tk.NO)
tree.column("#1", minwidth=0, width=100, stretch=tk.NO)
tree.column("#2", minwidth=0, width=100, stretch=tk.NO)
tree.grid()

# Place the Treeview widget at the bottom of the window
tree.grid(row=5, column=0, columnspan=2, sticky="nsew")
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

#Creating  textboxes
AdmNo = tk.Entry(root, width=30)
AdmNo.grid(row=0, column=1, padx=30)

Name = tk.Entry(root, width=30)
Name.grid(row=1, column=1)

Class = tk.Entry(root, width=30)
Class.grid(row=2, column=1)

#Creating  labels
AdmNo_label = tk.Label(root, text="Admission Number")
AdmNo_label.grid(row=0, column=0)

Name_label = tk.Label(root, text="Name")
Name_label.grid(row=1, column=0)

Class_label = tk.Label(root, text="Class")
Class_label.grid(row=2, column=0)

# Gets the value entered by the user in the textboxes
#====== here replace with your fields and you can add more
AdmNo_val = AdmNo.get()  # e.g. Phone Number
Name_val = Name.get()   # Furst name name
Class_val = Class.get()

textboxes = [AdmNo, Name, Class]

def connectAndAdd():
    # Connects to the database and adds  data to the database
    conn = sqlite3.connect('Payments.db')
    cursor = conn.cursor()  # creating a cursor object to execute commands

    # Create a table in the database
    cursor.execute('''CREATE TABLE IF NOT EXISTS Payments (AdmNo INT PRIMARY KEY, Name TEXT, Class INT)''')
    # =====cursor.execute('''CREATE TABLE IF NOT EXISTS Guardian_Contacts (Phone_No INT PRIMARY KEY, First_Name TEXT, Last_name TEXT)''')

    # Prepared insert stmt
    insert_query = "INSERT INTO Payments VALUES (?,?,?)"
    #====== insert_query = "INSERT INTO Guardian_Directory VALUES (?,?,?)" # this will depend with number of fields you have

    # Inserting data into table
    cursor.execute(insert_query, (AdmNo.get(), Name.get(), Class.get()))
    #====== replace with your variables
    # cursor.execute(insert_query, (Phone_No.get(), First_Name.get(), Class.get()))

    conn.commit()   #commits any chages made

    cursor.close()
    conn.close()   #closes the DB connection

# Function to submit the data
def submit():
    connectAndAdd()
    
    print("Data submitted")
    
    #this clears data in evry tetxboxes after submitting data
    for tb in textboxes:
        tb.delete(0, "end")

def query():
    # Connects to the database and adds  data to the database
    conn = sqlite3.connect('Payments.db')
    cursor = conn.cursor()  # creating a cursor object to execute commands

    # Fetch all records from the table
    cursor.execute("SELECT * FROM Payments")

    # Fetch all the records as a list of tuples
    records = cursor.fetchall()

    # Insert the records into the Treeview
    for record in records:
        tree.insert("", "end", values=record)

    conn.commit()   #commits any chages made

    cursor.close()
    conn.close()   #closes the DB connection
#Creating Buttons
# Create Submit button
submit_btn = tk.Button(root, text="Add", command=submit)
submit_btn.grid(row=3)

# Create Query button
query_btn = tk.Button(root, text="Show records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()
