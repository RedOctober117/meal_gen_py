from tkinter import *
from tkinter import ttk
from db_commands import *

class NullValue(Exception):
    pass

def flash_db(*args):
    try:
        flash_db_build(flash_path, connection)
    except:
        print("F")
        pass

def repair_db(*args):
    try:
        non_flash_db_build(non_flash_path, connection)
    except:
        print("F")
        pass

def add_unit_of_measure(*args):
    try:
        unit_name_value = unit_name.get()
        unit_abbrev_value = unit_abbrev.get()
        if unit_name_entry == '' | unit_abbrev_entry == '':
            raise NullValue('One or more entries were null.')
        query_add_unit_of_measure(unit_name_value, unit_abbrev_value, connection)
        print("Success")
    except:
        print("Failure")
        pass


# s = ttk.Style()
# s.configure('TFrame', background='#3b4252')
# nord_style.theme_settings("default", {
#     "TCombobox": {
#         "map": {
#             "background": [("active", "#3b4252"),
#                            ("!disabled", "#3b4252")],
#             "fieldbackground": [("!disabled", "#e5e9f0")],
#             "foreground": [("focus", "#4c566a"),
#                            ("!disabled", "#4c566a")]
#         }
#     }
# })



root = Tk()
root.title("Meal DB GUI")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Unit Name").grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Unit Abbrev").grid(column=1, row=2, sticky=(W, E))

unit_name = StringVar()
unit_name_entry = ttk.Entry(mainframe, width=7, textvariable=unit_name)
unit_name_entry.grid(column=2, row=1, sticky=(W, E))

unit_abbrev = StringVar()
unit_abbrev_entry = ttk.Entry(mainframe, width=7, textvariable=unit_abbrev)
unit_abbrev_entry.grid(column=2, row=2, sticky=(W, E))

success = StringVar()
ttk.Label(mainframe, textvariable=success).grid(column=3, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Submit", command=add_unit_of_measure).grid(column=3, row=2, sticky=E)
ttk.Button(mainframe, text="Repair DB", command=flash_db).grid(column=4, row=1, sticky=E)
ttk.Button(mainframe, text="Flash DB", command=repair_db).grid(column=4, row=2, sticky=E)

# s = ttk.Style()
# s.configure('TLabel', background='#3b4252', foreground='#eceff4')
# s.configure('TButton', background='#2e3440', foreground='#eceff4')
# s.configure('TFrame', background='#3b4252')
# s.configure('TEntry', lightcolor='#4c566a')

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

unit_name_entry.focus()
root.bind("<Return>", add_unit_of_measure)

root.mainloop()