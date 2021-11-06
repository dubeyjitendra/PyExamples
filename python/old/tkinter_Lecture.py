# #### Control
#     # Label
#     # Button
#     # Checkbox
#     # Combobox
#     # entry
# #####
# # Radio button
# # TextArea or ScrolledText
# # Spin Spinbox
# # Progressbar
# # List Box
# # File Upload Control
# # SetUp
# # Table # Will discuss next later

#  GUI Programming
    # Tkinter
    # WxPython
    # PyQt


# tkinter

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import ttk
#

# create a title
# win=Tk()
# win.title("First tkinter page")
# win.mainloop()



# create a title
# win=Tk()
# win.title("First tkinter page")
# #win.geometry("600x600")
# width,height= win.winfo_screenwidth(),win.winfo_screenheight()
# print(width,height)
# win.geometry("%dx%d"%(width,height))
# win.mainloop()


# Label
#
# win=Tk()
# win.title("First tkinter page")
# win.geometry("600x600")
# # width,height= win.winfo_screenwidth(),win.winfo_screenheight()
# # print(width,height)
# # win.geometry("%dx%d"%(width,height))
# lbl=Label(win,text="My Label",bg="red",fg="black")
# lbl.grid(column=2,row=2)
# win.mainloop()


# Entry
# win=Tk()
# win.title("First tkinter page")
# win.geometry("600x600")
# # width,height= win.winfo_screenwidth(),win.winfo_screenheight()
# # print(width,height)
# # win.geometry("%dx%d"%(width,height))
# txtbox=Entry(win,text="My Label",bg="white",fg="black",font=("arial",18),width=100)
# txtbox.grid(column=2,row=2)
# win.mainloop()


# # Button
# win=Tk()
# win.title("First tkinter page")
# win.geometry("600x600")
# # width,height= win.winfo_screenwidth(),win.winfo_screenheight()
# # print(width,height)
# # win.geometry("%dx%d"%(width,height))
# button=Button(win,text="Exit",command=win.quit)
# button.grid(column=2,row=2)
# #button.pack()
# win.mainloop()

# # Combo box
# win=Tk()
# win.title("First tkinter page")
# win.geometry("600x600")
# combobox=Combobox(win,width=20)
# combobox['value']= ["Pankaj","Jyoti","Sneha"]
# combobox.current(0)
# combobox.grid(column=2,row=2)
# win.mainloop()


# Check box
# window = Tk()
# window.geometry('350x200')
# var1 = IntVar()
# Male = Checkbutton(window, text='Male' ,variable=var1)
# var2 = IntVar()
# Female = Checkbutton(window, text='Female',variable=var2)
# def getvalue():
#     if var1.get()==1:
#         messagebox.showinfo("Msg","Male")
#     else:
#         messagebox.showinfo("Msg", "FeMale")
# Button(window,text="Submit",command=getvalue).grid(column=0,row=2)
# Male.grid(column=0, row=0)
# Female.grid(column=1, row=0)
# window.mainloop()


# # Radio box
# window = Tk()
# window.geometry('350x200')
# var1 = BooleanVar()
# Male = Radiobutton(window, text='Male' ,value=var1)
# var2 = BooleanVar()
# Female = Radiobutton(window, text='Female',value=var2)
# def getvalue():
#     print(var1.get())
#     if var1.get()==0:
#         messagebox.showinfo("Msg","Male")
#     if var2.get() == 1:
#         messagebox.showinfo("Msg", "FeMale")
# Button(window,text="Submit",command=getvalue).grid(column=0,row=2)
# Male.grid(column=0, row=0)
# Female.grid(column=1, row=0)
# window.mainloop()



#
# # Spin box
# def add():
#     firstname = Label(window, text=sp.get()).grid(row=2)
# window = Tk()
# window.geometry('350x200')
# sp=Spinbox(window,from_=100,to_=1000,width=30)
# Button(window,text="Submit",command=add).grid(column=0,row=1)
# sp.grid(column=0,row=0)
# window.mainloop()


# Text Area

# window = Tk()
# window.geometry('350x200')
# txt = scrolledtext.ScrolledText(window, width=40, height=10)
# txt.insert(INSERT,'Start from here!!!')
# txt.grid(column=0, row=0)
# window.mainloop()




# username with password
#
# def show_entry_fields():
#
#    if(m1.get() == 'tanmay' and m2.get() == "123"):
#        messagebox.showinfo("Login info", "login successfully")
#    else:
#        messagebox.showerror("Login error", "Login Incorrect")
#
# win = Tk()
# win.geometry("350x250")
# Label(win, text="user").grid(row=0)
# Label(win, text="password").grid(row=1)
# m1 = Entry(win,width=10)
# m2 = Entry(win,show="*",width=10)
# m1.grid(row=0, column=1)
# m2.grid(row=1, column=1)
# Button(win, text='Exit', command=win.quit).grid(row=3, column=0, sticky=W)
# Button(win, text='display', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# mainloop()



# Progress Bar
# window = Tk()
# window.geometry('450x300')
# style = ttk.Style()
# #style='red.Horizontal.TProgressbar'
# bar = Progressbar(window, length=400,style='TProgressbar') # , style='red.Horizontal.TProgressbar'
# bar['value'] = 45
# bar.grid(column=0, row=0)
# window.mainloop()



# def donothing():
#     filewin = Toplevel(root)
#     button = Button(filewin, text="Do nothing button")
#     button.pack()
#
# root=Tk()
# width, height = root.winfo_screenwidth(), root.winfo_screenheight()
# #root.geometry("200x100")
# root.geometry("%dx%d"%(width,height))
# #win.geometry("{}x{}".format(width,height))
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu1 = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Exit", command=root.destroy)
# menubar.add_cascade(label="Help", menu=filemenu1,command = root.destroy)
# root.config(menu=menubar)
# root.mainloop()


# # Table
# from tkinter import *
# import csv
#
# def createStandardTable(f, window):
#     handle = csv.reader(f)
#     length = len(next(handle))
#
#     sizes = [0] * length
#     for record in handle:
#
#         for p, column in enumerate(record):
#             if len(column) > sizes[p]:
#                 sizes[p] = len(column) + 3
#
#     f.seek(0)
#     trow = 0
#     table = Frame(window)
#     for record in handle:
#         for w, column in enumerate(record):
#             Label(table, text=column, width=sizes[w], borderwidth=2, relief="groove", justify=LEFT, anchor=W,
#                   background='white').grid(column=w, row=trow, sticky=W)
#
#         trow += 1
#
#     return table
#
#
# window = Tk()
# f = open("films.csv")
# var=createStandardTable(f,window)
# var.pack()
# window.mainloop()


# File Upload

# from tkinter import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename
# root = Tk(  )
# root.geometry("500x400")
# #This is where we lauch the file manager bar.
# def OpenFile():
#     name = askopenfilename(initialdir="C:/Users/",
#                            filetypes =(("Text File", "*.txt"),("All Files","*.*")),
#                            title = "Choose a file."
#                            )
#     #print (name)
#     #Using try in case user types in unknown file or closes without choosing a file.
#     try:
#         with open(name,'r') as UseFile:
#             print(UseFile.read())
#     except:
#         print("No file exists")
#
#
# '''Title = root.title( "File Opener")
# label = ttk.Label(root, text ="jitendra!!!",foreground="red",font=("Helvetica", 16))
# label.pack()'''
# #Menu Bar
# menu = Menu(root)
# root.config(menu=menu)
# file = Menu(menu)
# file.add_command(label = 'Open', command = OpenFile)
# file.add_command(label = 'Exit', command = lambda:exit())
# menu.add_cascade(label = 'File', menu = file)
# root.mainloop()


"""from tkinter import *
import pymysql
db=pymysql.connect("127.0.0.1","root","Abcd#1234","testdb")

# connection statement
try:
    cur=db.cursor()
    print("Connected {}".format(cur))
except ConnectionAbortedError as conerror:
    print(conerror)
# Fill details about textbox
def show_entry_fields():

   firstname=Label(win, text="First Name :"+e1.get(), bg="white").grid(row=5)
   lastname = Label(win, text="Last Name :"+e2.get(), bg="white").grid(row=6)
   print("First Name: %s\nLast Name: %s" % (e1.get(),e2.get()))
   # Create table
   sql = 
       create table studentlogs(
       firstname char(200),
       lastname char(20)
       ) 
       
   cur.execute(sql)
   sql="INSERT INTO studentlogs(firstname,lastname)VAlUES('"+e1.get()+"','"+e2.get()+"')"
   cur.execute(sql)
   db.commit()
   cur.close()"""


# File upload

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

class App(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.text = Text()
        self.text.pack()

        menu = Menu(master)
        root.config(menu=menu)
        # file menu
        filemenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="Save", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.do_exit)

    def file_open(self):
        """open a file to read"""
        # optional initial directory (default is current directory)
        initial_dir = "C:\temp"
        # the filetype mask (default is all files)
        mask = \
            [("Text and Python files", "*.txt *.py *.pyw"),
             ("HTML files", "*.htm"),
             ("All files", "*.*")]
        fin = askopenfile(initialdir=initial_dir, filetypes=mask, mode='r')
        text = fin.read()
        if text != None:
            self.text.delete(0.0, END)
            self.text.insert(END, text)

    def file_save(self):
        """get a filename and save the text in the editor widget"""
        # default extension is optional, here will add .txt if missing
        fout = asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(self.text.get(0.0, END))
        fout.write(text2save)
        fout.close()

    def do_exit(self):
        root.destroy()


root = Tk()
root.title("a very simple editor")
root.geometry('1000x600')
app = App(root)
root.mainloop()