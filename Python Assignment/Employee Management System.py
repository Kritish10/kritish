from tkinter import *
from tkinter import ttk
import pickle

import os


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def delete5():
    add_employee_screen.destroy()


def delete6():
    add_department_screen.destroy()


def add_employee():
    global add_employee_screen
    add_employee_screen = Toplevel(root)
    add_employee_screen.geometry("400x400")

    global id
    global id_entry
    global employeeName
    global employeeName_entry
    global age
    global age_entry
    global address
    global address_entry
    global contact
    global contact_entry
    global department
    global department_combobox

    id = StringVar()
    employeeName = StringVar()
    age = StringVar()
    address = StringVar()
    contact = StringVar()
    department = StringVar()

    add_employee_screen.title("Employee Registration Form")
    Label(add_employee_screen, text="Please Enter The Detail Below", bg="red", width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(text="").pack()

    Label(add_employee_screen, text="ID").pack()
    id_entry = Entry(add_employee_screen, textvariable=id)
    id_entry.pack()

    Label(add_employee_screen, text="Name").pack()
    employeeName_entry = Entry(add_employee_screen, textvariable=employeeName)
    employeeName_entry.pack()

    Label(text="").pack()

    Label(add_employee_screen, text="Age").pack()
    age_entry = Entry(add_employee_screen, textvariable=age)
    age_entry.pack()

    Label(text="").pack()

    Label(add_employee_screen, text="Address").pack()
    address_entry = Entry(add_employee_screen, textvariable=address)
    address_entry.pack()

    Label(text="").pack()

    Label(add_employee_screen, text="Contact").pack()
    contact_entry = Entry(add_employee_screen, textvariable=contact)
    contact_entry.pack()

    Label(text="").pack()

    data = read_from_pickle('department_info.txt')
    data_list = []
    count = 0

    for item in data:
        if count % 2 == 1:
            data_list.append(item)
        count += 1

    Label(add_employee_screen, text="Department").pack()
    department_combobox = ttk.Combobox(
        add_employee_screen, textvariable=department,
        values=data_list)
    department_combobox.pack()

    Button(add_employee_screen, text="Submit", width=10, height=1, command=save_employee).pack()
    Button(add_employee_screen, text="Reset", width=10, height=1, command=reset).pack()


def save_employee():

    id_info = id_entry.get()
    name_info = employeeName_entry.get()
    age_info = age_entry.get()
    address_info = address_entry.get()
    contact_info = contact_entry.get()
    department_info = department_combobox.get()
    data = [id_info, name_info, age_info, address_info, contact_info, department_info]

    PICKLE_FILE = "employee_info.txt"
    add_to_pickle(PICKLE_FILE, data)

    delete5()


def view_employee():

    global view_employee_screen
    view_employee_screen = Toplevel(root)
    view_employee_screen.title("Employee List")
    view_employee_screen.geometry("350x400")

    width = 6
    data = read_from_pickle('employee_info.txt')
    data_list = []

    for item in data:
        data_list.append(item)


    height = len(data_list)

    Label(view_employee_screen, text="ID", borderwidth=2).grid(row=0, column=0, padx=1, pady=1)
    Label(view_employee_screen, text="Name", borderwidth=2).grid(row=0, column=1, padx=1, pady=1)
    Label(view_employee_screen, text="Age", borderwidth=2).grid(row=0, column=2, padx=1, pady=1)
    Label(view_employee_screen, text="Address", borderwidth=2).grid(row=0, column=3, padx=1, pady=1)
    Label(view_employee_screen, text="Contact", borderwidth=2).grid(row=0, column=4, padx=1, pady=1)
    Label(view_employee_screen, text="Department", borderwidth=2).grid(row=0, column=5, padx=1, pady=1)
    count = 0

    for data in data_list:  # Rows


        for c in range(width):  # Columns4
            if c == 0:
                Label(view_employee_screen, text=data[0]).grid(row=count + 1, column=c, padx=1, pady=1)
            if c == 1:
                Label(view_employee_screen, text=data[1]).grid(row=count + 1, column=c, padx=1, pady=1)
            if c == 2:
                Label(view_employee_screen, text=data[2]).grid(row=count + 1, column=c, padx=1, pady=1)
            if c == 3:
                Label(view_employee_screen, text=data[3]).grid(row=count + 1, column=c, padx=1, pady=1)
            if c == 4:
                Label(view_employee_screen, text=data[4]).grid(row=count + 1, column=c, padx=1, pady=1)
            if c == 5:
                Label(view_employee_screen, text=data[5]).grid(row=count + 1, column=c, padx=1, pady=1)

        count += 1


def reset():
    id_entry.delete(0, END)
    employeeName_entry.delete(0, END)
    age_entry.delete(0, END)
    address_entry.delete(0, END)
    contact_entry.delete(0, END)
    department_combobox.delete(0, END)


def add_department():
    global add_department_screen
    global department_code
    global department_name
    global department_code_entry
    global department_name_entry
    global code_label

    add_department_screen = Toplevel(root)
    add_department_screen.geometry("400x400")
    department_code = StringVar()
    department_name = StringVar()

    add_department_screen.title("Department Form")
    Label(add_department_screen, text="Please Enter The Detail Below", bg="red", width="300", height="2",
          font=("Calibri", 13)).pack()

    Label(text="").pack()
    Label(add_department_screen, text="Department Code").pack()

    department_code_entry = Entry(add_department_screen, textvariable=department_code)
    department_code_entry.pack()

    Label(text="").pack()

    Label(add_department_screen, text="Department Name").pack()
    department_name_entry = Entry(add_department_screen, textvariable=department_name)
    department_name_entry.pack()

    Button(add_department_screen, text="Submit", width=10, height=1, command=save_department).pack()
    Button(add_department_screen, text="Reset", width=10, height=1, command=resett).pack()


def save_department():

    department_code_info = department_code_entry.get()
    department_name_info = department_name_entry.get()

    PICKLE_FILE = "department_info.txt"
    add_to_pickle(PICKLE_FILE, department_code_info)
    add_to_pickle(PICKLE_FILE, department_name_info)



    delete6()


def view_department():

    global department_screen
    department_screen = Toplevel(root)
    department_screen.title("Department List")
    department_screen.geometry("300x300")

    width = 2
    data = read_from_pickle('department_info.txt')
    data_list = []
    for item in data:
        data_list.append(item)

    Label(department_screen, text="ID", borderwidth=2).grid(row=0, column=0, padx=1, pady=1)
    Label(department_screen, text="  Department Name", borderwidth=2).grid(row=0, column=1, padx=1, pady=1)
    item_number = 0
    for r in range(int(len(data_list) / 2)):
        for c in range(width):  # Columns
            Label(department_screen, text=data_list[item_number]).grid(row=r + 1, column=c, padx=1, pady=1)
            item_number += 1


def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass


def add_to_pickle(path, item):
    with open(path, 'ab') as file:
        pickle.dump(item, file, pickle.HIGHEST_PROTOCOL)


def resett():
    department_code_entry.delete(0, END)
    department_name_entry.delete(0, END)


def login_sucess():
    screen2.destroy()
    global root
    root = Toplevel(screen)
    root.geometry("500x500")
    root.title("Main Screen")
    menubar = Menu(root)

    employeemenu = Menu(menubar, tearoff=0)
    employeemenu.add_command(label="Add Employee", command=add_employee)
    employeemenu.add_command(label="View Employee", command=view_employee)
    menubar.add_cascade(label="Employee", menu=employeemenu)

    departmentmenu = Menu(menubar, tearoff=0)
    departmentmenu.add_command(label="Add Department", command=add_department)
    departmentmenu.add_command(label="View Department", command=view_department)
    menubar.add_cascade(label="Department", menu=departmentmenu)

    logoutmenu = Menu(menubar, tearoff=0)
    logoutmenu.add_command(label="Logout", command=logout)
    menubar.add_cascade(label="Action", menu=logoutmenu)

    root.config(menu=menubar)
    # root.mainloop()


def logout():
    root.destroy()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Successful")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Successful")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():

    username_info = username.get()
    password_info = password.get()

    data = [username_info, password_info]

    PICKLE_FILE = username_info
    add_to_pickle(PICKLE_FILE, data)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucessfull", fg="green", font=("calibri", 11)).pack()


def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()


    if username1 in list_of_files:

        data = read_from_pickle(username1)

        for item in data:
            if password1 in item:
                login_sucess()
            else:
                password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter the required details").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter the required details to login", bg="green").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show="*")
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Login or Registration")
    Label(text="Login or Registration", bg="yellow", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()