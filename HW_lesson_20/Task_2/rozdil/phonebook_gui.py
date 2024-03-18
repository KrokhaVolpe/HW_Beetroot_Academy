import tkinter as tk
from tkinter import ttk, messagebox, Label, Entry, Button
from tkinter.ttk import Combobox
from phonebook_logic import PhonebookApp

class PhonebookGUI:
    def __init__(self, phonebook_app):
        self.phonebook_app = phonebook_app
        #self.root = tk.Tk()
        self.setup_gui()

    def setup_gui(self):
        # Colors
        color_0 = '#ffffff'
        color_1 = '#272630'
        color_2 = '#3498DB'

        self.root = tk.Tk()
        self.root.title('')
        self.root.geometry('485x450')
        self.root.configure(background=color_0)
        self.root.resizable(width=False, height=False)

        # Frames
        frame_up = tk.Frame(self.root, width=500, height=70, bg=color_1)
        frame_up.place(x=0, y=0)

        frame_down = tk.Frame(self.root, width=500, height=150, bg=color_0)
        frame_down.place(x=0, y=70)

        frame_table = tk.Frame(self.root, width=500, height=100, bg=color_0, relief='flat')
        frame_table.place(x=10, y=220)

        #frames_up
        self.app_name = Label(frame_up, text='Контакти', height=1, font=('Verdana 17 bold'), bg=color_1, fg=color_0)
        self.app_name.place(x=10, y=20)

        #frames_dowт
        self.label_name = Label(frame_down, text="Ім'я *", width=20, height=1, font=('Ivy 10'), bg=color_0, anchor=tk.NW)
        self.label_name.place(x=10, y=20)
        self.e_name = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
        self.e_name.place(x=55, y=20)

        self.label_last_name = Label(frame_down, text="Прізвище", width=20, height=1, font=('Ivy 10'), bg=color_0, anchor=tk.NW)
        self.label_last_name.place(x=10, y=50)
        self.e_last_name = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
        self.e_last_name.place(x=85, y=50)

        self.label_telephone = Label(frame_down, text="Телефон *", height=1, font=('Ivy 10'), bg=color_0, anchor=tk.NW)
        self.label_telephone.place(x=10, y=80)
        self.e_label_telephone = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
        self.e_label_telephone.place(x=85, y=80)

        self.label_city = Label(frame_down, text="Місто", height=1, font=('Ivy 10'), bg=color_0, anchor=tk.NW)
        self.label_city.place(x=10, y=110)
        self.e_label_city = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
        self.e_label_city.place(x=55, y=110)
        
        #Buttons
        button_search = Button(frame_down, text="Знайти ", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0, command=lambda: self.search_entry())
        button_search.place(x=380, y=20)
        self.e_search = Entry(frame_down, width=17, justify='left', highlightthickness=1, relief='solid', font=('Ivy 10'))
        self.e_search.place(x=250, y=20)

        button_add = Button(frame_down, text="Додати", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0,  command=self.phonebook_app.add_entry)
        button_add.place(x=380, y=50)

        button_update = Button(frame_down, text="Оновити", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0, command=self.phonebook_app.update_entry)
        button_update.place(x=380, y=80)

        button_delete = Button(frame_down, text="Видалити", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0,  command=self.phonebook_app.delete_entry)
        button_delete.place(x=380, y=110)

        button_restore = Button(frame_down, text="Відновити", height=1, width=15, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0, command=self.phonebook_app.restore_database)
        button_restore.place(x=250, y=80)

        # Table
        columns = ("Ім'я", "Прізвище", "Телефон", "Місто")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings", selectmode="browse")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110)  

        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.tree.config(yscrollcommand=scrollbar.set)

        # Combobox for search field selection
        search_fields = ("ПІБ", "Ім'я", "Прізвище", "Телефон", "Місто")
        self.search_field_var = tk.StringVar()
        search_combobox = Combobox(frame_down, values=search_fields, textvariable=self.search_field_var, state="readonly", width=17)
        search_combobox.place(x=250, y=50)
        search_combobox.set(search_fields[0])  
       
        self.update_table()

    def update_table(self):
    # Clear existing data from the table
        for row in self.tree.get_children():
            self.tree.delete(row)

    # Populate the table with data from the phonebook
        for entry in self.phonebook_app.phonebook_data:
            self.tree.insert("", "end", values=(entry.get("name", ""), entry.get("last_name", ""), entry.get("telephone", ""), entry.get("city", "")))


    def add_entry(self):
        entry = {
            'name': self.e_name.get(),
            'last_name': self.e_last_name.get(),
            'telephone': self.e_label_telephone.get(),
            'city': self.e_label_city.get()
        }
    
        self.phonebook_app.add_entry(entry)
        

    def search_entry(self):
        query = self.e_search.get()
        # Викликаємо метод search_entry класу PhonebookApp та передаємо параметр query
        results = self.phonebook_app.search_entry(query)
        # Додайте код для відображення результатів

    def update_entry(self):
        entry = {
            'name': self.e_name.get(),
           'last_name': self.e_last_name.get(),
            'telephone': self.e_label_telephone.get(),
            'city': self.e_label_city.get()
        }
        index = self.get_selected_index()  # Ви повинні створити цю функцію для отримання індексу вибраного запису
        self.phonebook_app.update_entry(index, entry)

    def delete_entry(self):
        index = self.get_selected_index()  # Ви повинні створити цю функцію для отримання індексу вибраного запису
        self.phonebook_app.delete_entry(index)




if __name__ == "__main__":
    try:
        phonebook_name = "phonebook.json"
        app_logic = PhonebookApp(phonebook_name)
        app_gui = PhonebookGUI(app_logic)
        app_gui.root.mainloop()
    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))
    except ValueError as e:
        messagebox.showerror("Error", str(e))
