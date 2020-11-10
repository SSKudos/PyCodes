from tkinter import *
import tkinter.filedialog
import os
import urllib.request
import urllib
from time import strftime
import tkinter.messagebox
from tkinter import colorchooser
import time
from tkinter.filedialog import asksaveasfile

def Kreg():
    try:
        m= myText.delete(1.0, "end")
        web= Ent.get()
        x = urllib.request.urlopen(web)
        f= x.read()
        r= myText.insert(END, f)
    except:
        f= myText.insert(END, "Error try again later")

root= Tk()
#root.geometry("800x800+500+500")
#root.resizable(width= False, height= False)
Tit = root.title('KUDOS BROWSER')


#Tit.configure(font= 'Helvetica 24 bold italic')
#frame = Frame(root)
#localtime= time.asctime(time.localtime(time.time()))
def timer():
    stri= strftime('%H:%M:%S %p')
    lab1.config(text = stri)
    lab1.after(1000, timer)

butt1 = Button(root, text= 'Go', relief= 'raised', command= Kreg)
butt1.grid(row= 1,column=0, sticky='w')

lab1 = Label(root, text= timer)
lab1.grid(row= 0, columnspan= 2, sticky= W)
timer()

Ent = Entry(root,width= 70)
Ent.grid(row= 1, column=2,padx= 4, sticky= 'ew')

myText = Text(root, foreground="#D6D6D6", wrap='word') #background='#101010',
myText.insert(END, "GOD HELP ME ACHIEVE ALL MY DREAMS, NO LET MY EFFORTS BE IN VAIN IN JESUS NAME. AMEN")
scrollBar = Scrollbar(orient= "vertical")
#connect them to each other
myText.configure(yscrollcommand= scrollBar.set)
scrollBar.configure(command=myText.yview)
myText.grid(row=2, columnspan=3, sticky= W+E+N+S)
scrollBar.grid(row= 2, column=3, sticky= 'ns' )

#==========Menu=========
def quit_app():
    root.quit()

def open_file():
    input_file_name= tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                       filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt" )])
    if input_file_name:
        file_name= input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), Tit))
        myText.delete(1.0, END)
        with open(file_name) as _file:
            myText.insert(1.0, _file.read())

def new_file():
    root.title('Untitled')
    myText.delete(1.0, END)

def file_save():
    f= tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if f is None:
        return
    txt2save= myText.get(1.0, END)
    f.write(txt2save)
    f.close()

menubar = Menu(root)
fmenu= Menu(menubar,tearoff= False)
fmenu.add_command(label= 'Open', command= open_file)
fmenu.add_command(label= 'Save', command= file_save)
fmenu.add_command(label= 'New File', command= new_file)
fmenu.add_separator()
fmenu.add_command(label= 'Quit', command= quit_app)
menubar.add_cascade(menu=fmenu, label= 'File')

root.config(menu=menubar)

#=============EditMenu
def getColor():
    (rgb, hx)= colorchooser.askcolor(title= 'Choose color')
    myText.config(bg=hx)

editmenu= Menu(menubar, tearoff=0)
editmenu.add_command(label= 'Cut')
editmenu.add_command(label= 'Copy')
editmenu.add_command(label= 'Paste')
editmenu.add_command(label= 'Choose color', command= getColor)
editmenu.add_command(label= 'Find')
menubar.add_cascade(label='Edit', menu=editmenu)

#============ViewMenu
def file_path():
    path= Ent.get()
    for (path, dirs, files)in os.walk(path):
        for fn in files:
            rot = os.path.join(path, fn)
            size = int(os.stat(rot).st_size/(1024*1024))
            if(size > 300):
                myText.insert(1.0, view_folder())        #print(fn + ' ' + str(size) + 'mb')
            else:
                myText.insert(1.0,'An error occured')

def view_folder():
    newWin = Toplevel(root)
    boxx= Listbox(newWin, height= 10)
    boxx.pack()


viewmenu= Menu(menubar, tearoff=0)
viewmenu.add_command(label='Downloads', command= file_path)
viewmenu.add_command(label='View Folders', command= view_folder)
menubar.add_cascade(label='View', menu=viewmenu)

#=================HelpMenu
def Dloads():
    cur_dir = os.getcwd()
    print('Downloading files')
    url= Ent.get()
    urllib.request.urlretrieve(url, cur_dir)

def diplayMsgBox():
    tkinter.messagebox.showinfo("About", "{}{}".format(Tit, "Tkinter GUI Development"))
def HelpMsgBox():
    H=tkinter.messagebox.askquestion("Help", "Do you like this App", icon='question')
    if H == 'yes':
        myText.delete(1.0, END)
        myText.insert(1.0, 'Thank you')
    else:
        myText.delete(1.0, END)
        myText.insert(1.0, 'We will try to make it better')

helpmenu= Menu(menubar, tearoff=0)
helpmenu.add_command(label='About', command= diplayMsgBox)
helpmenu.add_command(label='Help', command= HelpMsgBox)
helpmenu.add_command(label='Download', command= Dloads)
menubar.add_cascade(label='Help', menu=helpmenu)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#butt1.pack(side= LEFT)
#Ent.pack(fill= BOTH)
root.mainloop()
