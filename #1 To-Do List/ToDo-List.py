from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as sql

def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values (?)', (task_string,))    
        list_update()    
        task_field.delete(0, 'end')  
    
def list_update():    
    clear_list()    
    for task in tasks:    
        task_listbox.insert('end', task)  
  
def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:  
            tasks.remove(the_value)    
            list_update()   
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:    
        while(len(tasks) != 0):    
            tasks.pop()    
        the_cursor.execute('delete from tasks')   
        list_update()  
   
def clear_list():   
    task_listbox.delete(0, 'end')  
  
def close():    
    print(tasks)   
    guiWindow.destroy()  
    
def retrieve_database():    
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
   
if __name__ == "__main__":   
    guiWindow = Tk()   
    guiWindow.title("To-Do List")  
    guiWindow.geometry("700x500+550+250")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg="#D3D3D3")  # Light grey background
    
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 12), padding=10)
    style.configure("TEntry", font=("Helvetica", 12))
    style.configure("TListbox", font=("Helvetica", 12))

    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  
    
    tasks = []  
    
    functions_frame = Frame(guiWindow, bg="#D3D3D3", padx=10, pady=10) 
    functions_frame.pack(side="top", expand=True, fill="both")  
    
    task_label = ttk.Label(functions_frame, text="Enter the Task Title:")    
    task_label.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        
    task_field = ttk.Entry(functions_frame, width=50)    
    task_field.grid(row=0, column=1, pady=10, padx=10)  
    
    add_button = ttk.Button(functions_frame, text="Add", command=add_task)  
    del_button = ttk.Button(functions_frame, text="Remove", command=delete_task)  
    del_all_button = ttk.Button(functions_frame, text="Delete All", command=delete_all_tasks)  
    exit_button = ttk.Button(functions_frame, text="Exit / Close", command=close)  
    
    add_button.grid(row=1, column=0, pady=10, padx=10, sticky=EW)  
    del_button.grid(row=1, column=1, pady=10, padx=10, sticky=EW)  
    del_all_button.grid(row=2, column=0, pady=10, padx=10, sticky=EW)  
    exit_button.grid(row=2, column=1, pady=10, padx=10, sticky=EW)  
    
    task_listbox = Listbox(functions_frame, width=70, height=15, font=("Helvetica", 12), bg="white", fg="black", selectbackground="#ADD8E6", selectforeground="black")    
    task_listbox.grid(row=3, column=0, columnspan=2, pady=10, padx=10)  
    
    retrieve_database()  
    list_update()    
    guiWindow.mainloop()    
    the_connection.commit()  
    the_cursor.close()
