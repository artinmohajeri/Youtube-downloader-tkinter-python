from tkinter import *
from utilities import *
from tkinter.filedialog import askdirectory
from pytube import YouTube
from tkinter import messagebox

win = Tk()
win.geometry("600x380")
win.resizable(0,0)
win.title("Artin Youtube Downloader")
win.iconbitmap("./Youtube_logo.ico")
win.configure(bg="red")
win.columnconfigure(0, weight=1)
video_link = StringVar()
clicked = StringVar()
clicked.set("144p")
qualities = [
    "144p",
    "240p",
    "360p",
    "480p",
    "720p",
    "1080p",
]

def widgets():
    global address_input, link_input, download_btn
    link_label = Label(win, text="Video Link: ", font=("None",16), pady=10, bg="red")
    link_label.grid(row=0, column=0)
    link_input = Entry(win, width=40, font=("none",12))
    link_input.grid(row=1, column=0, ipady=4)
    link_input.bind("<Button-3>",show_menu)
    drop_down = OptionMenu(win,clicked, *qualities)
    drop_down.grid(row=2, column=0, pady=(10,0))

    address_label = Label(win, text="Directory Adress: ", font=("None",16), bg="red")
    address_label.grid(row=3, column=0, pady=(50, 0))
    address_input = Entry(win, width=40, font=("none",12))
    address_input.grid(row=4, column=0, ipady=4)
    address_input.bind("<Button-3>",show_menu2)

    open_btn = Button(win, text="Open", relief="ridge", width=15, height=1, command=browse)
    open_btn.grid(row=5,column=0, pady=(10,0))
    download_btn = Button(win, text="Download", relief="ridge", width=25, height=2, bg="green", fg="white", command=download)
    download_btn.grid(row=6,column=0, pady=(50,0))

def browse():    
    global address
    address_input.delete(0, END)
    address = askdirectory(initialdir="YOUR DIRECTORY PATH", title="save")
    address_input.insert(0,address)

def download():
    if link_input.get() and address_input.get():
        try:
            youtube_link = YouTube(link_input.get())
            youtube_link.streams.filter(res=f"{clicked.get()}").first().download(address)
            messagebox.showinfo(title="Success", message="your video is downloaded successully!!")
        except:
            messagebox.showerror(title="Error", message="The video link or quality is not found")
    else:
        messagebox.showerror(title="Error", message="Please fill out the form completely!")


widgets()
enable_right_click(link_input)
enable_right_click2(address_input)
win.mainloop()