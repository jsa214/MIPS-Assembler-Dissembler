########################Jihoon Sung (Chengzhixun) 3160300021#
#***********************************************************#
#*********************GUI(Assembler.exe).py*****************#
#***********************************************************#
#******************************************2018-04-30*******#
#***********************************************************#


#use 'tkinter'
from tkinter import*
import sys, string, os


window = Tk()
#geometry etcetc, straight forward when open the exe
window.title("3160300021.Jihoon Sung Assembler")
window.geometry("400x400")
window.configure(bg="white")
label = Label(window,text = "Please Enter Mips Instruction")
label.configure(bg='white')
label.place(x= 50, y=25)

#for the gui program, the examples to look at
label1 = Label(window,text = "Ex1:  Sub $s0 $s1 $s2")
label1.configure(bg='white')
label1.place(x= 50, y=45)
label2 = Label(window, text="Ex2:  Label1: And $v0 $v1 $a0")
label2.configure(bg='white')
label2.place(x= 50, y=65)
label3 = Label(window, text="Ex3:   or $a0 $a3 $zero")
label3.configure(bg='white')
label3.place(x= 50, y=85)
label4 = Label(window, text="*Can copy and paste multiple lines of Mips Code")
label4.configure(bg='white')
label4.place(x= 50, y=105)

Student=[]

label = Label(window, text="Mips Code")
label.configure(bg='white')
label.place(x=50, y=140)
entry_box2=Entry(window,)
entry_box2.place(x=115, y=140)

# Function to add user input into the text file

def adduser():
    addstudent = open ("MipsCodeToAssemble.txt", "w")
    addstudent.write(entry_box2.get())
    addstudent.close ()

    window.destroy()


#function to button
b = Button(window, borderwidth=2, text="Enter", width=12, pady=5, command=adduser)
b.place(x=110,y=185)

window.mainloop()

os.system("use1.exe")

root = Tk()

#now the program opens assembledhex and read it out
with open("AssembledHex.txt", "r") as f:
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    #****Uses scrollbar
    mylist = Listbox(root, yscrollcommand=scrollbar.set)
    for line in range(300):
        mylist.insert(END, f.readline())
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)



    root.title("3160300021.Jihoon Sung Assembler")
    root.geometry("300x300")

root.mainloop()
