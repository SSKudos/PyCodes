#Merge videos
from tkinter import *
import tkinter.filedialog
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
import concurrent.futures

root = Tk()
root.title("Video Merger")
root.geometry("600x600")


def Merger():
	clip1 = VideoFileClip(Ent2.get())
	clip2 = VideoFileClip(Ent3.get())
	clip = concatenate_videoclips([clip1, clip2])
	clip = clip.write_videofile(Ent1.get(), threads=4, logger= None)

with concurrent.futures.ThreadPoolExecutor() as executor:
	results = [executor.submit(Merger) for _ in range(10)]

def open_file():
    input_file_name= tkinter.filedialog.askopenfilename(defaultextension=".mp4",
                                       filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt" )])
    Ent2.insert(END, input_file_name)

def open_file2():
    input_file_name= tkinter.filedialog.askopenfilename(defaultextension=".mp4",
                                       filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt" )])
    Ent3.insert(END, input_file_name)


Y = StringVar()
frame1 = Frame(root)
frame1.pack(side= TOP)
But1 = Button(frame1,text= "New Name")
But1.pack(side= LEFT)
Ent1 = Entry(frame1, width= 50, textvariable= Y)
Ent1.pack(side= LEFT)

x = StringVar()
frame2 =Frame(root)
frame2.pack(side= TOP)
But2 = Button(frame2, text= "Browse", command= open_file)
But2.pack(side=LEFT)
Ent2 = Entry(frame2, width=50, textvariable= x)
Ent2.pack(side= LEFT)

z = StringVar()
frame3 = Frame(root)
frame3.pack(side= TOP)
But3 = Button(frame3,text= "Browse", command= open_file2)
But3.pack(side= LEFT)
Ent3 = Entry(frame3, width= 50, textvariable= z)
Ent3.pack(side= LEFT)

frame3 = Frame(root)
frame3.pack(side= TOP)
But3 = Button(frame3,text= "Merge Video",command= Merger)
But3.pack(side= LEFT)


root.mainloop()
