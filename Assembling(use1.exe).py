########################Jihoon Sung (Chengzhixun) 3160300021#
#***********************************************************#
#*********************Assembler.py**************************#
#***********************************************************#
#******************************************2018-04-30*******#
#***********************************************************#
#**Converts contents (Mips Code) in "MipsCodeToAssemble.txt"#
#**into hexadecimal in "AssembledHex.txt"*******************#


def filelen(fname):
    #Function to measure the number of lines in a file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



def dec_to_bin(x):
    #Function to convert decimal to binary
    s=format(x,'05b')
    return s




def Regtobin(form):
    #Function to convert
    #the save to binary
    if (form[0] == '$'):
        if (form[1] == 'z'):
            # in case of zero
            reg1 = 0
            newreg = '00000'
            #print(newreg)
            return (str(newreg))


        if (form[1] == 'v'):
            # in case of valuesfor results and expression eva
            reg1 = 2 + int(form[2])
            newreg = dec_to_bin(int(reg1))
            #print(newreg)
            return (str(newreg))


        if (form[1] == 'a'):
            # in case of arguments
            reg1 = 4 + int(form[2])
            newreg = dec_to_bin(int(reg1))
            #print(newreg)
            return (str(newreg))


        if (form[1]=='s'):
            if(form[2]!='p'):
                #in case of saved
                reg1=16+int(form[2])
                newreg=dec_to_bin(int(reg1))
                #print(newreg)
                return(str(newreg))
            else:
                #in case of sp
                reg1=29
                newreg = dec_to_bin(int(reg1))
                #print(newreg)
                return (str(newreg))

        if (form[1]=='t'):
            #in case of temp
            if(int(form[2])<8):
                reg1=8+int(form[2])
                newreg = (str(dec_to_bin(int(reg1))))
                #print(newreg)
                return (str(newreg))
            else:
                reg1=16+int(form[2])
                newreg = dec_to_bin(int(reg1))
                #print(newreg)
                return (str(newreg))

        if (form[1]=='g'):
            #in case of gp
            reg1=28
            newreg=dec_to_bin(int(reg1))
            #print(newreg)
            return(str(newreg))

        if (form[1]=='f'):
            #in case of fp
            reg1=30
            newreg=dec_to_bin(int(reg1))
            #print(newreg)
            return(str(newreg))

        if (form[1]=='r'):
            #in case of rp
            reg1=31
            newreg=dec_to_bin(int(reg1))
            #print(newreg)
            return(str(newreg))
    else:
        newreg=dec_to_bin(int(form))
        #print(newreg)
        return(str(newreg))




#Instruction conversion
def Add(first, second, third):
    #Add function
    
    h=(int('000000'+Regtobin(second)+Regtobin(third)+Regtobin(first)+'00000'+'100000',2))
    return("{0:#0{1}x}".format(h, 10))



def Sub(first, second, third):
    #Sub function
    h=(int('000000' + Regtobin(second) + Regtobin(third) + Regtobin(first) + '00000' + '100010', 2))
    return("{0:#0{1}x}".format(h, 10))


def And(first, second, third):
    #And function

    h=(int('000000' + Regtobin(second) + Regtobin(third) + Regtobin(first) + '00000' + '100100', 2))
    return("{0:#0{1}x}".format(h, 10))

def Or(first, second, third):
    #Or function

    h=(int('000000' + Regtobin(second) + Regtobin(third) + Regtobin(first) + '00000' + '100101', 2))
    return("{0:#0{1}x}".format(h, 10))

def Sll(first, second, third):
    #Sll function
    h=(int('000000'+'00000' + Regtobin(second) + Regtobin(first) + Regtobin(third) + '000000', 2))

    return("{0:#0{1}x}".format(h, 10))

def Srl(first, second, third):
    #Srl function
    h = (int('000000' + '00000' + Regtobin(second) + Regtobin(first) + Regtobin(third) +  '000010', 2))
    return("{0:#0{1}x}".format(h, 10))

def Slt(first, second, third):
    #Slt function

    h=(int('000000' + Regtobin(second) + Regtobin(third) + Regtobin(first) + '00000' + '101010', 2))
    return("{0:#0{1}x}".format(h, 10))

def Jr(first):
    #Jr function

    h=(int('000000' + Regtobin(first) + '00000' + '00000'+ '00000'+ '001000', 2))
    return("{0:#0{1}x}".format(h, 10))

def J(first, location):
    #J function

    touse=str(format(eval(first),'026b'))
    h=(int('000010'+touse,2))
    return ("{0:#0{1}x}".format(h, 10))


def Jal(first, location):
    #Jal function
    touse = str(format(eval(first), '026b'))
    h = (int('000011' + touse, 2))
    return ("{0:#0{1}x}".format(h, 10))

def Addi(first, second, third):
    #Addi
    if int(third)<0:
        return(Subi(first, second, third))

    else:
        third=int(third)
        third=format(third, '016b')
        h = (int('001000' + Regtobin(second)+Regtobin(first)  + str(third), 2))
        return ("{0:#0{1}x}".format(h, 10))

def Subi(first, second, third):
    #Subi
    third=int(third)
    third=bin(third & 0xffff)[2:]
    h = (int('001000' + Regtobin(second)+Regtobin(first)  + str(third), 2))
    return ("{0:#0{1}x}".format(h, 10))

def Ori(first, second, third):
    #Ori
    third = int(third)
    third = format(third, '016b')
    h = (int('001101' + Regtobin(second)+Regtobin(first)  + str(third), 2))
    return ("{0:#0{1}x}".format(h, 10))

def Lw(first, second):
    #Lw
    new = second.split('(')
    second=new[0]
    second = format(int(second), '016b')
    third=new[1].strip(')')
    h = (int('100011' + Regtobin(third)+Regtobin(first)+str(second), 2))
    return ("{0:#0{1}x}".format(h, 10))

def Sw(first, second):
    #Sw
    new = second.split('(')
    second=new[0]
    second = format(int(second), '016b')
    third=new[1].strip(')')
    h = (int('101011' + Regtobin(third)+Regtobin(first)+str(second), 2))
    return ("{0:#0{1}x}".format(h, 10))

def Lui(first, second):
    #Lui
    second*(2**16)
    second = int(second)
    second = format(second, '016b')
    h = (int('001111'+'00000' + Regtobin(first)+str(second), 2))
    return ("{0:#0{1}x}".format(h, 10))

def Slti(first, second, third):
    #Slti
    third=int(third)
    third=format(third, '016b')
    h = (int('001010' + Regtobin(second)+Regtobin(first)  + str(third), 2))
    return ("{0:#0{1}x}".format(h, 10))

def Beq(first, second, third, i):
    #beq
    dist=(eval(third)-i-1)
    if (dist)<0:
        return(BeqBackward(first, second, dist, i))
    else:
        third = str(format(dist, '016b'))
        #print('000100' +Regtobin(first)+ Regtobin(second)+ str(third))
        h = (int('000100' +Regtobin(first)+ Regtobin(second)+ str(third), 2))
        return ("{0:#0{1}x}".format(h, 10))

def BeqBackward(first, second, third, i):
    #in case of branching backward
    third = bin(third & 0xffff)[2:]
    h = (int('000100' + Regtobin(first) + Regtobin(second) + str(third), 2))
    return ("{0:#0{1}x}".format(h, 10))

def Bne(first, second, third, i):
    #bne
    dist = (eval(third) - i - 1)
    if (dist) < 0:
        return (BneBackward(first, second, dist, i))
    else:
        third = str(format(dist, '016b'))
        h = (int('000101' + Regtobin(first) + Regtobin(second) + str(third), 2))
        return ("{0:#0{1}x}".format(h, 10))

def BneBackward(first, second, third, i):
    #incase has to branch to backward
    third = bin(third & 0xffff)[2:]
    h = (int('000101' + Regtobin(first) + Regtobin(second) + str(third), 2))
    return ("{0:#0{1}x}".format(h, 10))


def write(new,i):
    #Function to write into assembledhex text file according to instruction
    if (new[0] == "Add") or (new[0]=="Sub") or (new[0]=="And") or (new[0]=="Or") or (new[0]=="Sll") or (new[0]=="Srl") or (new[0]=="Slt") or (new[0]== "Addi") or (new[0]=="Ori") or (new[0]=="Slti"):

        a=new[0]
        save=eval(a)(new[1], new[2], new[3])
        hex = open("AssembledHex.txt", "a")
        hex.write(save[2:])
        hex.write("\n")
        hex.close()
    elif (new[0] == "Jr") :
        a = new[0]
        save = eval(a)(new[1])
        hex = open("AssembledHex.txt", "a")
        hex.write(save[2:])
        hex.write("\n")
        hex.close()
    elif (new[0]== "J") or (new[0]=="Jal") :
        a = new[0]
        save = eval(a)(new[1], i)
        hex = open("AssembledHex.txt", "a")
        hex.write(save[2:])
        hex.write("\n")
        hex.close()
    elif (new[0] == "Beq") or (new[0] == "Bne"):
        a = new[0]
        save = eval(a)(new[1], new[2], new[3],i)
        hex = open("AssembledHex.txt", "a")
        hex.write(save[2:])
        hex.write("\n")
        hex.close()
    elif (new[0]=="Lw") or (new[0]=="Sw") or (new[0]=="Lui"):
        a = new[0]
        save = eval(a)(new[1], new[2])
        hex = open("AssembledHex.txt", "a")
        hex.write(save[2:])
        hex.write("\n")
        hex.close()


#MAIN FUNCTION
        
with open("MipsCodeToAssemble.txt","r") as f:
    #THE GUI takes user input to 'the above text file
    save=[line.rstrip('\n') for line in f]
    hex = open("ignore1.txt", "w").close()
    for i in range (0,filelen("MipsCodeToAssemble.txt")):
        new=save[i].split()
        new[0]=new[0].title()
        #If there is label, save the label and the line number
        while new[0] not in ["Add","Sub","And","Or","Addi","Ori","Sll","Srl","Lw","Sw","Lui","Slt","Slti","Beq","Bne","J","Jal","Jr"]:
            name = (new[0])
            name = name[:-1]
            globals()[name] = i
            del new[0]
        tosave=" ".join(new)
        #create another text file called ignore1 and save all the lines without labels
        hex = open("ignore1.txt", "a")
        hex.write(tosave)
        hex.write("\n")
    hex.close()
    #Save result into assembledhex text
    hex = open("AssembledHex.txt", "w").close()
    with open("ignore1.txt", "r") as fi:
        save2 = [line.rstrip('\n') for line in fi]
        for j in range(0, filelen("MipsCodeToAssemble.txt")):
            new = save2[j].split()
            write(new,j)
    import os
    #remove ignore1 textfile
    os.remove("ignore1.txt")
