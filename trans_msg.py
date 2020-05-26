from tkinter import *
from tkinter import messagebox

window = Tk() #setup the app object by calling the Tk() function

def if_send():
    label_id = Label(window, text="sss:(hex)", font=("arial", 9, "bold"))
    label_id.place(x=50, y=50)

# ID Label
label_id = Label(window, text="ID:(hex)", font=("arial", 9, "bold"))
label_id.place(x=10, y=10)

# ID Input
entry_id = Entry(width=10)
entry_id.place(x=10, y=30)

# ID Output
label_id = Label(window, text="ID:(hex)", font=("arial", 9, "bold"))
label_id.place(x=10, y=10)


# Send Button
btn_ok = Button(window, text="OK", width=12, bg='white', fg='black', command=if_send)
btn_ok.place(x=150, y=200)

# Cancel Button
btn_cancel = Button(window, text="cancel", width=12, bg='white', fg='black')
btn_cancel.place(x=280, y=200)

# Window Widgets
window.title('New Transmit Message')
window.geometry("500x300+10+20") #window.geometry("width x height + XPOS +Y POS")
window.mainloop()


