#!/usr/bin/env python3
import os, time, queue
from threading import Thread
from tkinter import * 
import tkinter as tk
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle
from tkinter import messagebox, scrolledtext
from time import strftime, gmtime
from tkinter import font as tkFont
#from jobSearchForGui import job_search
from scripts.jobsSearch import job_search

FLAG = 0

pages = {1: 'search_frame', 2: 'return_frame'}

def get_jobs(frame):
    create_search_frame.search_button.config(state="disabled")
    
    create_search_frame.progress_bar.start(interval=50)
    
    search_label_var = tk.StringVar()
    search_label_var = "Searching for Jobs ..."
    search_label = Label(frame, text=search_label_var).grid(row=4, column=2, pady=10)
    
    get_jobs.jobs_returned = job_search(create_search_frame.search_variable.get())
    create_search_frame.progress_bar.stop()
    
    # insert jobs found into text area
    return_page.text_area.insert(tk.INSERT, get_jobs.jobs_returned)
    create_search_frame.search_button.config(state="normal")
    
    
    # Change frames 
    return_frame.tkraise()

def swap(frame):
    swap.job_title = create_search_frame.search_variable.get()
    swap.company = create_search_frame.company_variable.get()

    print(str(frame))
    '''
    if str(frame) == '.results':
        create_search_frame.search_button.config(state="disabled")
        
        jobs_returned = job_search(swap.job_title)
        #my_thread = threading.Thread(target=get_jobs).setart()

        return_page.text_area.insert(tk.INSERT, jobs_returned)
        create_search_frame.search_button.config(state="active")
    '''
    frame.tkraise()


def clicked(frame):
    Thread(target=get_jobs, args=(frame,)).start()

def create_search_frame(app):
   frame = ttk.Frame(app, name="job Search")

   title_frame = ttk.Frame(frame)
   title_frame.grid(row=0, column=0)
   
   label_frame = ttk.Frame(frame)
   label_frame.grid(row=1, column=0, sticky="NSEW")
   
   s = ttk.Style()
   s.configure('entry.TFrame', background="yellow", foreground="yellow")
   s.configure('entry.TLabel', background="yellow", foreground="yellow")
   
   #entry_frame = ttk.Frame(frame, style="entry.TFrame")
   #entry_frame.grid(row=2, column=0)
   
   '''
   for i in range(3):
       label_frame.columnconfigure(i, weight=1)
    
   label_frame.rowconfigure(1, weight=1)
   '''
   
   window_title = ttk.Label(frame, text="Job Search Tool", font=("SF Pro Rounded", 24))
   window_title.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")
   
   # ================================ Job Label ================================
   job_label = ttk.Label(label_frame, text="Job Title: ", font=("SF Pro Rounded Thin", 14))
   job_label.grid(row=0, column=1, padx=5, sticky="E")
   
    # ================================ Drop Down Label ================================
   company_label = ttk.Label(label_frame, text="Company: ", font=("SF Pro Rounded Thin", 14), anchor=CENTER)
   company_label.grid(row=1, column=1, padx=5, sticky="E")
   
   # ================================ Entry Box Widget ================================
   create_search_frame.search_variable = StringVar(app)
   search = ttk.Entry(label_frame, font=("SF Pro Rounded Thin", 14), textvariable=create_search_frame.search_variable)
   search.grid(row=0, column=2, pady=5, sticky="NSEW")
   
   
   # ================================ Drop Down Widget ================================
   create_search_frame.company_variable = StringVar(app)
   company_combobox = ttk.Combobox(label_frame, font=("SF Pro Rounded Thin", 14), textvariable=create_search_frame.company_variable)
   company_combobox['values'] = ("Booz Allen Hamilton", "Trend Micro")
   company_combobox.grid(row=1, column=2, pady=5, sticky="NSEW")

   create_search_frame.progress_bar = ttk.Progressbar(label_frame, orient=HORIZONTAL, length=300, mode='indeterminate')
   create_search_frame.progress_bar.grid(row=3, column=2, padx=5)

   
   # ================================ Search Button ================================
   #create_search_frame.search_button = ttk.Button(label_frame, text="Search", command=lambda: swap(return_frame))
   create_search_frame.search_button = ttk.Button(label_frame, text="Search", command=lambda: clicked(label_frame))
   create_search_frame.search_button.grid(row=2, column=2, pady=5)
   
   return frame

def return_page(app):
    frame = ttk.Frame(app, name="results")
    
    label_frame = ttk.Frame(frame)
    label_frame.grid(row=0, column=0)
    
    label = ttk.Label(label_frame, text="Results", font=("SF Pro Rounded", 24), anchor=CENTER)
    label.grid(row=0, column=1, padx=5, pady=5, sticky="NSEW")
    
    # button frame
    button_frame = ttk.Frame(frame)
    button_frame.grid(row=1, column=0, padx=(10, 0 ), pady=(10, 0), sticky="EW")
    
    # text frame
    text_frame = ttk.Frame(button_frame, width="10")
    text_frame.grid(row=2, column=1, padx=(5, 0 ), pady=(5, 0), sticky="NS")
    
    # ================================ ScrolledText Widget ================================
    return_page.text_area = scrolledtext.ScrolledText(text_frame, font=('SF Pro Rounded Thin', 8),
                                          wrap=tk.WORD,
                                          height=30, width=70
                                          )
    return_page.text_area.grid(row=0, column=0, padx=5, pady=5, sticky="NS")

    #return_page.text_area.insert(tk.INSERT, "hhhhh")
    #return_page.text_area.configure(state="disabled")
    
    # ================================ Back Button ================================
    go_back_button = ttk.Button(button_frame, width=7, text="Go Back", command=lambda: swap(search_frame))
    go_back_button.grid(row=0, column=1, padx=5, pady=1, sticky="N")
    
    return frame

app = Tk()
app.title('Job Search')
app.geometry('500x525')
#app.resizable(0, 0)

app.columnconfigure(0, weight=1)
app.rowconfigure(1, weight=1)


style = ttk.Style(app)
#app.tk.call('source', '/Users/nicholausbrell/python/ttk themes/Azure-ttk-theme-main/azure-dark.tcl')
#style.theme_use('azure-dark')
app.tk.call('source', '/Users/nicholausbrell/python/ttk themes/Forest-ttk-theme-master/forest-dark.tcl')
style.theme_use('forest-dark')


search_frame = create_search_frame(app)
search_frame.grid(row=0, column=0, sticky="nsew")


return_frame = return_page(app)
return_frame.grid(row=0, column=0, sticky="nsew")

for i in range(3):
       search_frame.columnconfigure(i, weight=1)
       return_frame.columnconfigure(i, weight=1)
    
search_frame.rowconfigure(1, weight=1)
return_frame.rowconfigure(1, weight=1)

footer = "Made by NickBrell" + " "*130
#footer = " "*165 + "\nHello"
tk.Label(app, text=footer, font=("SF Pro Rounded", 14), bg="#0fbe7a").grid(row=3, column=0, sticky="W", columnspan=3)
#tk.Label(app, text="footer", font=("SF Pro Rounded", 14), bg="#7f39fb", anchor=SW).grid(row=1, column=0, sticky="NSEW", columnspan=3)

search_frame.tkraise()
#return_frame.tkraise()
app.mainloop()