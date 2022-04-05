from tkinter import *
import wikipedia 

root =Tk()
root.geometry("800x600")
root.title("Krawler")
root.resizable(0, 0)


def clear():
    global search_bar
    global text
    search_bar.delete(0, END)
    text.delete(1.0, END)


def search():
    global search_bar
    global text

    try:
        query = search_bar.get()
        clear()
        data = wikipedia.page(query)
        text.insert(END, data.content)

    except Exception as e:
        text.insert(END, e)


labelframe = LabelFrame(root, text="DISCOVERER", width=50, font=("Consolas, 10"), bg="grey")
labelframe.pack(pady=10)

search_bar = Entry(labelframe, width=50)
search_bar.pack(pady=10)

frame = Frame(root)
frame.pack(padx=10)

vert_scroll = Scrollbar(frame)
vert_scroll.pack(fill=Y, side=RIGHT)

text = Text(frame, undo=True, yscrollcommand=vert_scroll.set, fg="white", bg="#333333",
            font=("Consolas, 10"), width=800)
text.pack()

vert_scroll.config(command=text.yview)

btn_frame = Frame(root, bg="grey")
btn_frame.pack(pady=5)

clear_btn =  Button(btn_frame, text="Clear", bg="green", fg="#363636", font=("Helvetica", 20), 
                    command=lambda: clear())
clear_btn.grid(row=0, column=0, padx=30, pady=30)


search_btn =  Button(btn_frame, text="Search", bg="green", fg="#363636",font=("Helvetica", 20), 
                     command=lambda: search())
search_btn.grid(row=0, column=2)


root.config(bg="grey")
root.mainloop()