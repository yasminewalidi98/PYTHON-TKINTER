from __future__ import print_function
from tkinter import *
import tkinter.messagebox as msg
import can

window = Tk()

def send_msg():
    ID = ID_input.get()
    Lenght = Lenght_input.get()
    Cycle_time = Cycle_time_input.get()
    Data = Data1_input.get()+Data2_input.get()+Data3_input.get()+Data4_input.get()+Data5_input.get()+Data6_input.get()+Data7_input.get()+Data8_input.get()

    bus = can.interface.Bus(bustype='vector',app_name=None , channel=0, bitrate=500000)
    msg = can.Message(arbitration_id=ID,
                      data=[0x02,0x11,0x02,0x00 ,0x00 ,0x00, 0x00, 0x00],dlc=3,
                      extended_id=False)
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent")

def show_answer():
    ID = ID_input.get()
    Lenght = Lenght_input.get()
    Cycle_time = Cycle_time_input.get()
    Data = Data1_input.get()+Data2_input.get()+Data3_input.get()+Data4_input.get()+Data5_input.get()+Data6_input.get()+Data7_input.get()+Data8_input.get()
    msg.showinfo(title=None,
    message="You send:\nID: '"+ID+"'\nLenght: '"+Lenght+"'\nCycle time: '"+Cycle_time+"'\nData: '"+Data+"'")

# ID:(hex)
Label(window, text = "ID:(hex)", font=("arial", 9, "bold")).grid(row=0, column=0)
ID_input = Entry(window, width=10)
ID_input.place(x=0, y=20)

# Lenght
Label(window, text="Lenght:", font=("arial", 9, "bold")).place(x=180, y=0)
Lenght_input = Entry(window, width=9)
Lenght_input.place(x=180, y=20)

# Cycle time
Label(window, text="cycle time", font=("arial", 9, "bold")).place(x=0, y=40)
Label(window, text="ms", font=("arial", 6, "bold")).place(x=80, y=60)
Cycle_time_input = Entry(window,width=10)
Cycle_time_input.place(x=0,y=60)

# Data:(hex)
Label(window, text="Data:(hex)", font=("arial", 9, "bold")).place(x=300, y=0)
Data1_input = Entry(window, width=2)
Data1_input.place(x=300, y=20)
Data2_input = Entry(window, width=2)
Data2_input.place(x=320, y=20)
Data3_input = Entry(window, width=2)
Data3_input.place(x=340, y=20)
Data4_input = Entry(window, width=2)
Data4_input.place(x=360, y=20)
Data5_input = Entry(window, width=2)
Data5_input.place(x=380, y=20)
Data6_input = Entry(window, width=2)
Data6_input.place(x=400, y=20)
Data7_input = Entry(window, width=2)
Data7_input.place(x=420, y=20)
Data8_input = Entry(window, width=2)
Data8_input.place(x=440, y=20)

# Message Type
Checkbutton(window, text="send extended ", font=("arial", 9, "bold")).place(x=200, y=40)
Checkbutton(window, text="send ", font=("arial", 9, "bold")).place(x=200, y=60)

# Buttons
Button(window, text='Send', command=send_msg).place(x=150, y=200)
Button(window, text='Cancel', command=window.destroy).place(x=280, y=200)

# Window Widgets
window.geometry("500x300")
window.title("Transmit message")
window.mainloop()

