import tkinter
root = tkinter.Tk()
root.geometry("800x600")
root.title("初めてのキャンバス")
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()


def click_btn():
    button["text"] = "クリックしました"

button = tkinter.Button(root, text="クリックしてください", font=(
    "Times New Roman", 24), command=click_btn)
button.place(x=200, y=100)
root.mainloop()
