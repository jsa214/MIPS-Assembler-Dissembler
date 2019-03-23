########################Jihoon Sung (Chengzhixun) 3160300021#
#***********************************************************#
#*********************GUI(Dissembler.exe).py****************#
#***********************************************************#
#******************************************2018-04-30*******#
#***********************************************************#


#uses tkinter
from tkinter import*
import sys, string, os


window = Tk()

#geometry etcetc, straight forward when open the exe
window.title("3160300021.Jihoon Sung Dissembler")
window.geometry("400x400")
window.configure(bg="white")
label = Label(window,text = "Please Enter Hex Representation of Mips")
label.configure(bg='white')
label.place(x= 50, y=25)
#for the gui program, the examples to look at
label1 = Label(window,text = "Ex1:  112c0007")
label1.configure(bg='white')
label1.place(x= 50, y=45)
label2 = Label(window, text="Ex2:  21ac0005")
label2.configure(bg='white')
label2.place(x= 50, y=65)
label4 = Label(window, text="*Can copy and paste multiple lines of Code")
label4.configure(bg='white')
label4.place(x= 50, y=105)

Student=[]

label = Label(window, text="Hex Code")
label.configure(bg='white')
label.place(x=50, y=140)
entry_box2=Entry(window,)
entry_box2.place(x=115, y=140)

# Function
# Function to add user input into the text file
def adduser():
    addstudent = open ("HexToDissemble.txt", "w")
    addstudent.write(entry_box2.get())
    addstudent.close ()

    window.destroy()


#function to button
b = Button(window, borderwidth=2, text="Enter", width=12, pady=5, command=adduser)
b.place(x=110,y=185)

window.mainloop()

os.system("use2.exe")

root = Tk()
#now the program opens dissembled and read it out
with open("DissembledMips.txt", "r") as f:
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    #****Uses scrollbar
    mylist = Listbox(root, yscrollcommand=scrollbar.set)
    for line in range(300):
        mylist.insert(END, f.readline())
    mylist.pack(side=LEFT, fill=BOTH, expand=1)
   
    scrollbar.config(command=mylist.yview)



    root.title("3160300021.Jihoon Sung Assembler")
    root.geometry("500x500")

root.mainloop()
