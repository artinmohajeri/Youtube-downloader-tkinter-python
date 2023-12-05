from tkinter import Menu

def cut(inp):
    inp.event_generate("<<Cut>>")
def copy(inp):
    inp.event_generate("<<Copy>>")
def paste(inp):
    inp.event_generate("<<Paste>>")

def enable_right_click(inp):
    global menu
    menu = Menu(inp, tearoff=0)
    menu.add_command(label="Cut", command=lambda:cut(inp=inp))
    menu.add_command(label="Copy", command=lambda:copy(inp=inp))
    menu.add_command(label="Paste", command=lambda:paste(inp=inp))

def enable_right_click2(inp):
    global menu2
    menu2 = Menu(inp, tearoff=0)
    menu2.add_command(label="Cut", command=lambda:cut(inp=inp))
    menu2.add_command(label="Copy", command=lambda:copy(inp=inp))
    menu2.add_command(label="Paste", command=lambda:paste(inp=inp))

def show_menu(event):
    menu.post(event.x_root, event.y_root)
def show_menu2(event):
    menu2.post(event.x_root, event.y_root)