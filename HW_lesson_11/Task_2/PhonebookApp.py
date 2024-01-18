from tkinter import ttk
import tkinter as tk
from tkinter import messagebox, Label, Entry, Button
import json
from tkinter.ttk import Combobox


class PhonebookApp:
    def __init__(self, phonebook_name):
        self.phonebook_name = phonebook_name
        self.phonebook_data = self.load_phonebook_data()

        self.e_name = None
        self.e_last_name = None
        self.e_label_telephone = None
        self.e_label_city = None
        self.e_search = None

        self.create_gui()

    def load_phonebook_data(self):
        try:
            file_path = "phonebook.json"
            with open(file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("Phonebook data not found. Create a new phonebook.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in phonebook data.")

    def save_phonebook_data(self):
        file_path = "phonebook.json"
        with open(file_path, "w", encoding='utf-8') as file:
            json.dump(self.phonebook_data, file, indent=2)
            
    def create_gui(self):
        
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

        button_add = Button(frame_down, text="Додати", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0,  command=self.add_entry)
        button_add.place(x=380, y=50)

        button_update = Button(frame_down, text="Оновити", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0, command=self.update_entry)
        button_update.place(x=380, y=80)

        button_delete = Button(frame_down, text="Видалити", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0,  command=self.delete_entry)
        button_delete.place(x=380, y=110)

        button_restore = Button(frame_down, text="Відновити", height=1, width=15, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0, command=self.restore_database)
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

    def update_table(self, data=None):
        # Очистити таблицю перед оновленням
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Використовувати дані з параметру data або весь phonebook_data
        entries = data if data is not None else self.phonebook_data

        # Додати дані до таблиці
        for entry in entries:
            self.tree.insert("", "end", values=(entry.get("name", ""), entry.get("last_name", ""), entry.get("telephone", ""), entry.get("city", "")))

        return entries

    
    def add_entry(self):
        # Отримати дані з полів вводу
        name = self.e_name.get()
        last_name = self.e_last_name.get()
        telephone = self.e_label_telephone.get()
        city = self.e_label_city.get()
    
        # Додати новий запис до телефонної книги
        new_entry = {"name": name, "last_name": last_name, "telephone": telephone, "city": city}
        self.phonebook_data.append(new_entry)

        entries = self.update_table()

        self.e_name.delete(0, tk.END)
        self.e_last_name.delete(0, tk.END)
        self.e_label_telephone.delete(0, tk.END)
        self.e_label_city.delete(0, tk.END)

        self.save_phonebook_data()

    def search_entry(self):
        query = self.e_search.get().lower() 
        results = []

        for entry in self.phonebook_data:
            full_name = f"{entry.get('name', '').lower()} {entry.get('last_name', '').lower()}"
            if query in full_name:
                results.append(entry)
            elif any(query in value.lower() for value in entry.values()):
                results.append(entry)

        updated_entries = self.update_table(results)

        self.phonebook_data = updated_entries


    def update_entry(self):
        # Отримати вибраний елемент з Treeview
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select an entry to update.")
            return

        # Отримати індекс вибраного елемента
        selected_index = self.tree.index(selected_item)

        # Отримати дані для оновлення
        name = self.e_name.get()
        last_name = self.e_last_name.get()
        telephone = self.e_label_telephone.get()
        city = self.e_label_city.get()

        # Отримати значення поточного запису
        current_entry = self.phonebook_data[selected_index]

        # Оновити дані запису
        current_entry["name"] = name
        current_entry["last_name"] = last_name
        current_entry["telephone"] = telephone
        current_entry["city"] = city

        # Оновити таблицю із зміненими даними
        self.update_table()

        # Очистити поля вводу
        self.e_name.delete(0, tk.END)
        self.e_last_name.delete(0, tk.END)
        self.e_label_telephone.delete(0, tk.END)
        self.e_label_city.delete(0, tk.END)

        # Зберегти зміни у файл
        self.save_phonebook_data()


    def delete_entry(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Увага", "Виберіть запис, який потрібно видалити..")
            return

        selected_index = self.tree.index(selected_item)

        deleted_entry = self.phonebook_data.pop(selected_index)

        self.update_table()

        messagebox.showinfo("Видалено", f"Запис видалено:\n{deleted_entry}")

        self.save_phonebook_data()


    def restore_database(self):
        confirmation = messagebox.askyesno("Відновлення бази даних", "Ви впевнені, що хочете відновити всю базу даних? Це призведе до перезапису поточних даних.")
        if confirmation:
            self.phonebook_data = self.load_phonebook_data()

            self.update_table()

            self.e_search.delete(0, tk.END)





    def on_closing(self):
        # Зберегти дані в JSON перед закриттям
        self.save_phonebook_data()
        self.root.destroy()
        


try:
    phonebook_name = "phonebook.json"
    app = PhonebookApp(phonebook_name)
except FileNotFoundError as e:
    messagebox.showerror("Error", str(e))
except ValueError as e:
    messagebox.showerror("Error", str(e))
    
app.root.protocol("WM_DELETE_WINDOW", app.on_closing)
app.root.mainloop()

