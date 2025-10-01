# Import tkinter module
from tkinter import *
import os

def ins_app1():
    os.system("gnome-terminal -- bash install_app1.sh")
def ins_app2():
    os.system("gnome-terminal -- bash install_app2.sh")

# Create object
root = Tk()
# Adjust size
root.geometry( "800x600" )
root.resizable(False, False)
root.title("FTP App manager")

intro_label = Label(root, text = "FTP Application manager", font=("Arial", 30))
intro_label.place(x = 0, y = 0)
button1 = Button(root, text = "Install", command = ins_app1)
button1.place(x = 720, y = 80)
button1 = Button(root, text = "Install", command = ins_app2)
button1.place(x = 720, y = 150)



Solid_line_text1 = Label(root, text = "-" * 200)
Solid_line_text1.place(x = 0, y = 50)

App_1_label = Label(root, text = "*Insert app 1 name here*", font=("Arial", 20))
App_1_label.place(x = 10, y = 80)

Solid_line_text2 = Label(root, text = "-" * 200)
Solid_line_text2.place(x = 0, y = 120)

App_1_label = Label(root, text = "*Insert app 2 name here*", font=("Arial", 20))
App_1_label.place(x = 10, y = 150)

Solid_line_text3 = Label(root, text = "-" * 200)
Solid_line_text3.place(x = 0, y = 190)

Solid_line_text4 = Label(root, text = "-" * 200)
Solid_line_text4.place(x = 0, y = 50)

Solid_line_text5 = Label(root, text = "-" * 200)
Solid_line_text5.place(x = 0, y = 50)



# Execute tkinter
root.mainloop()
