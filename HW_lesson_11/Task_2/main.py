from tkinter import *
from tkinter import ttk
import json

# Colors
color_0 = '#ffffff'
color_1 = '#272630'
color_2 = '#3498DB'

window = Tk()
window.title('')
window.geometry('485x450')
window.configure(background=color_0)
window.resizable(width=FALSE, height=FALSE)

# Frames
frame_up = Frame(window, width=500, height=70, bg=color_1)
frame_up.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')

frame_down = Frame(window, width=500, height=150, bg=color_0)
frame_down.grid(row=1, column=0, padx=0, pady=0, sticky='nsew')

frame_table = Frame(window, width=500, height=100, bg=color_0, relief='flat')
frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky='nsew')

# Global Variables
tree = None
data = []
phonebook_name = 'phonebook.json'

# Functions
def load_data(phonebook_name):
    try:
        with open(phonebook_name, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError("Файл з даними не знайдено. Спробуйте створити новий телефонний довідник.")

def save_data(phonebook_name, data):
    with open(phonebook_name, 'w') as file:
        json.dump(data, file, indent=2)

def delete_button():
    telephone = e_label_telephone.get()
    try:
        global data
        data = delete_entry(data, telephone)
        save_data(phonebook_name, data)
        show_data(data)
    except ValueError as e:
        print(e)

def update_button_clicked():
    telephone = e_label_telephone.get()
    name = e_name.get()
    last_name = e_last_name.get()
    city = e_label_city.get()

    new_entry = {"Name": name, "Last name": last_name, "Telephone": telephone, "City": city}
    try:
        global data
        data = update_entry(data, telephone, new_entry)
        save_data(phonebook_name, data)
        show_data(data)
    except ValueError as e:
        print(e)

def show_data(data):
    tree.delete(*tree.get_children())
    for entry in data:
        tree.insert('', 'end', values=(entry['Name'], entry['Last name'], entry['Telephone'], entry['City']))

def show(): 
    global tree, data

    list_header = ["Name", "Last name", "Telephone", "City"]

    tree = ttk.Treeview(frame_table, selectmode='extended', columns=list_header, show='headings')

    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')

    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='nsew')

    tree.heading("Name", text="Ім'я", anchor=NW)
    tree.heading("Last name", text="Прізвище", anchor=NW)
    tree.heading("Telephone", text="Телефон", anchor=NW)
    tree.heading("City", text="Місто", anchor=NW)

    tree.column("Name", width=100, anchor='nw')
    tree.column("Last name", width=160, anchor='nw')
    tree.column("Telephone", width=130, anchor='nw')
    tree.column("City", width=180, anchor='nw')

    show_data(data)

show()

def add_entry(phonebook_name, data, entry):
    data.append(entry)
    save_data(phonebook_name, data)
    return data

def delete_entry(data, telephone):
    for entry in data:
        if entry['Telephone'] == telephone:
            data.remove(entry)
            return data
    raise ValueError("Запис з вказаним номером телефону не знайдено.")

def update_entry(data, telephone, new_entry):
    for i, entry in enumerate(data):
        if entry['Telephone'] == telephone:
            data[i] = new_entry
            return data
    raise ValueError("Запис з вказаним номером телефону не знайдено.")

def add_button():
    global data
    name = e_name.get()
    last_name = e_last_name.get()
    telephone = e_label_telephone.get()
    city = e_label_city.get()

    new_entry = {"Name": name, "Last name": last_name, "Telephone": telephone, "City": city}
    data = add_entry(phonebook_name, data, new_entry)
    show_data(data)
    


#frames_up
app_name = Label(frame_up, text='Контакти', height=1, font=('Verdana 17 bold'), bg=color_1, fg=color_0)
app_name.place(x=5, y=20)

#frames_down
label_name = Label(frame_down, text="Ім'я *", width=20, height=1, font=('Ivy 10'), bg=color_0, anchor=NW)
label_name.place(x=10, y=20)
e_name = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
e_name.place(x=55, y=20)

label_last_name = Label(frame_down, text="Прізвище", width=20, height=1, font=('Ivy 10'), bg=color_0, anchor=NW)
label_last_name.place(x=10, y=50)
e_last_name = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
e_last_name.place(x=85, y=50)

label_telephone = Label(frame_down, text="Телефон *", height=1, font=('Ivy 10'), bg=color_0, anchor=NW)
label_telephone.place(x=10, y=80)
e_label_telephone = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
e_label_telephone.place(x=85, y=80)

label_city = Label(frame_down, text="Місто", height=1, font=('Ivy 10'), bg=color_0, anchor=NW)
label_city.place(x=10, y=110)
e_label_city = Entry(frame_down, width=20, justify='left', highlightthickness=1, relief='solid')
e_label_city.place(x=55, y=110)

#Buttons
button_search = Button(frame_down, text="Знайти ", height=1,  width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0)
button_search.place(x=380, y=20)
e_search = Entry(frame_down, width=17, justify='left', highlightthickness=1, relief='solid',  font=('Ivy 10'))
e_search.place(x=250, y=20)


button_view = Button(frame_down, text="Переглянути", height=1, width=14,  font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0)
button_view.place(x=250, y=50)

button_add = Button(frame_down, text="Додати", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0)
button_add.place(x=380, y=50)

button_update = Button(frame_down, text="Оновити", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0)
button_update.place(x=380, y=80)

button_delete = Button(frame_down, text="Видалити", height=1, width=10, font=('Ivy 10 bold'), bg=color_2, fg=color_0, highlightthickness=0)
button_delete.place(x=380, y=110)

window.mainloop()
