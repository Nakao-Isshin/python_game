import tkinter
import tkinter.messagebox

def click_btn():
    # txt = entry.get()
    # button["text"] = txt
    
    # text.insert(tkinter.END, "monster appeared")
    tkinter.messagebox.showinfo("info", "button pressed")
    

def check():
    if cval.get():
        print("checked")
    else:
        print("not checked")

root = tkinter.Tk()
root.title("First text box")
root.geometry("400x200")
# entry = tkinter.Entry(width=20)
# entry.place(x=20, y=20)
button = tkinter.Button(text="get strings", command=click_btn)
# button.place(x=20, y=100)
button.pack()
cval = tkinter.BooleanVar()
cval.set(True)
cbtn = tkinter.Checkbutton(text="check_btn", variable=cval, command=check)
cbtn.place(x=20, y=20)
text = tkinter.Text()
# text.pack()
text.place(x=20, y=50, width=360, height=120)
root.mainloop()