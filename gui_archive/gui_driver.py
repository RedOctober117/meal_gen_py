from tkinter import *
from tkinter import ttk
from db_commands import *


def draw_treeview(parent, query):
    label = ttk.Label(parent, text=query)
    return label
    # query_result = query
    # query_length = len(query_result)
    # query_item_length = len(query_result[0])
    
    # treeview = ttk.Treeview(parent, columns=query_result[0], displaycolumns=query_item_length - 1)

    # for element in range(1, query_length):
    #     treeview.insert('', element, query_result[element], text=element)
    # return treeview


base_window = Tk()
base_window.title('Meal DB Editor')

mainframe = ttk.Frame(base_window, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


button1 = ttk.Button(mainframe, text='test')
button1.grid(column=0, row=0)

frame1 = ttk.Notebook(mainframe, width=100, height=100)

tree = draw_treeview(frame1, query_print_table('default_serving_units', 'unit_id, type, unit_of_measure_id', connection))

frame1.add(tree)
frame1.grid(column=1, row=0, sticky=(N, W, E, S))

# tree = ttk.Treeview(frame1)
# tree.insert('', 0, text='look at me')

base_window.columnconfigure(0, weight=1)
base_window.rowconfigure(0, weight=1)


mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)

base_window.mainloop()