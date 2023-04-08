import tkinter


def count_up():
    global tmr
    tmr += 1
    # label["text"] = tmr
    root.after(1000, count_up)


key = ""


def keydown(e):
    global key
    key = e.keysym
    print("KEY:"+str(key))


def keyup(e):
    global key
    key = ""


cx = 400
cy = 300


def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canvas.coords("MYCHR", cx, cy)
    # label["text"] = key
    root.after(100, main_proc)


tmr = 0
root = tkinter.Tk()
root.title("get keycode")
root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)
canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file="tutorial/mimi.png")
canvas.create_image(cx, cy, image=img, tag="MYCHR")
# label = tkinter. Label(font=("Times New Roman", 80))
# label.pack()
main_proc()
# root.after(1000, count_up)
root.mainloop()
