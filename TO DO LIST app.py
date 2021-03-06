from tkinter import*

obj = Tk()

obj.configure(bg="#FCE0DA")
obj.title("My To Do List")
obj.geometry("350x300")
tasks = []
def update_lb():
    clear_lb()
    for task in tasks:
        lb_tasks.insert("end",task)
def clear_lb():
    lb_tasks.delete(0,"end")

def add_task():
    task = text_input.get()
    if task!="":
        tasks.append(task)
        update_lb()
    else:
        display["text"]="Please enter a task."
    text_input.delete(0,"end")
def del_all():
    global tasks
    tasks = []
    update_lb()
def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_lb()
def sort_asc():
    tasks.sort()
    update_lb()
def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_lb()

def num_task():
    number_of_tasks=len(tasks)
    message = "Number of tasks : %s"%number_of_tasks
    display["text"]=message




title = Label(obj,text ="To-Do-List",bg = "#FCE0DA",font="sans-serif")
title.grid(row=0,column=0 )
display = Label(obj,text="",bg = "#FCE0DA")
display.grid(row= 0,column= 1)
text_input = Entry(obj,width = 15)
text_input.grid(row= 1,column= 1)

button_add_task = Button(obj, text = "Add Task",bg = "white" ,command = add_task )
button_add_task.grid(row= 1,column=0 )
button_del_all = Button(obj, text = "Delete All Tasks",bg = "white" ,command = del_all )
button_del_all.grid(row= 2,column= 0)
button_del = Button(obj, text = "Delete Task",bg = "white" ,command = del_one )
button_del.grid(row= 3,column= 0)
button_sort_asc = Button(obj, text = "Sort Task in Ascending Order" ,bg = "white" , command = sort_asc )
button_sort_asc.grid(row=4 ,column=0 )
button_sort_desc = Button(obj, text = "Sort Task in Descending Order" ,bg = "white" , command = sort_desc )
button_sort_desc.grid(row= 5,column= 0)

button_num_task = Button(obj, text = "Number Of Tasks" ,bg = "white" , command = num_task )
button_num_task.grid(row=7 ,column= 0)
button_exit = Button(obj, text = "Exit" ,bg = "white" , command = exit )
button_exit.grid(row= 8,column=0 )
lb_tasks = Listbox(obj,bg = "white" )
lb_tasks.grid(row= 2,column=1,rowspan=7 )

obj.mainloop()

