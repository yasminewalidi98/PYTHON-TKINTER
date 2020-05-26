from tkinter import *
from tkinter.messagebox import *

window = Tk() #setup the app object by calling the Tk() function

# show variable function
def show_answer():
    Ans = ID.get()
    Answer.insert(0, Ans)

# recorver vars
ID = Entry(window)
Test2 = Entry(window)
Answer = Entry(window)

# Labels
ID.grid(row=0, column=1)
Test2.grid(row=1, column=1)
Answer.grid(row=2, column=1)

Label(window, text = "ID:(hex)").grid(row=0)
Label(window, text = "Test 2:").grid(row=1)
Label(window, text = "The Answer is:").grid(row=2)

# Buttons
Button(window, text='Quit', command=window.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(window, text='Show', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)



# Window Widgets
window.title('New Transmit Message')
# window.geometry("500x300+10+20") #window.geometry("width x height + XPOS +Y POS")
window.mainloop()