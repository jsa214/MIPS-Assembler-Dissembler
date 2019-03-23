########################Jihoon Sung (Chengzhixun) 3160300021#
#***********************************************************#
#*********************Dissembler.py*************************#
#***********************************************************#
#******************************************2018-04-30*******#
#***********************************************************#
#**Converts contents (Mips Code) in "MipsCodeToAssemble.txt"#
#**into hexadecimal in "AssembledHex.txt"*******************#

#functions to use-----------------------------------------------------------
def filelen(fname):
    #Function to measure the number of lines in a file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#turn hex to binary
def hextobin(x):
    my_hexdata = x
    scale = 16  ## equals to hexadecimal
    num_of_bits = 32
    return(bin(int(my_hexdata, scale))[2:].zfill(num_of_bits))


#in case of subtraction or going backward, add twoscomplement function
def toTwosComplement(binarySequence):
    convertedSequence = [0] * len(binarySequence)
    carryBit = 1
    for i in range(0, len(binarySequence)):
        if binarySequence[i] == '0':
            convertedSequence[i] = 1
        else:
            convertedSequence[i] = 0
    if convertedSequence[-1] == 0: #if last digit is 0, just add the 1 then there's no carry bit so return
            convertedSequence[-1] = 1
            return ''.join(str(x) for x in convertedSequence)
    for bit in range(0, len(binarySequence)):
        if carryBit == 0:
            break
        index = len(binarySequence) - bit - 1
        if convertedSequence[index] == 1:
            convertedSequence[index] = 0
            carryBit = 1
        else:
            convertedSequence[index] = 1
            carryBit = 0
    return ''.join(str(x) for x in convertedSequence)




#write to file function
def write(value,i):
    binary=hextobin(value)
    tosave=decoding(binary,i)
    hex = open("step2.txt", "a")
    hex.write(tosave)
    hex.write("\n")
    hex.close()



#decoding function to three different types
def decoding(binary,i):
    if(binary[:6]=='000000'):
        return(R(binary))
    else:
        #J-----------------------
        if (binary[:6] == '000010') or (binary[:6] == '000011'):
            location=Jtype(binary)[0]
            nametouse="label"+str(location)
            globals()[nametouse]=Jtype(binary)[0]
            if Jtype(binary)[1]==1:
                return("J "+"label"+str(Jtype(binary)[0]))
            else:
                return("Jal "+"label"+str(Jtype(binary)[0]))

        # I----------------------
        else:
            return(I(binary,i))



#Three Types--------------------------------------------------------------------

def R(binary):
    if(binary[26:32]=="100000"):
        return(Add(binary))
    if(binary[26:32] == "100010"):
        return(Sub(binary))
    if (binary[26:32] == "100100"):
        return(And(binary))
    if (binary[26:32] == "100101"):
        return(Or(binary))
    if (binary[26:32] == "000000"):
        return(Sll(binary))
    if (binary[26:32] == "000010"):
        return(Srl(binary))
    if (binary[26:32] == "101010"):
        return(Slt(binary))
    if (binary[26:32] == "001000"):
        return(Jr(binary))

def I(binary,i):
    if(binary[:6] == '001000'):
        return(Addi(binary))
    if(binary[:6]=='001101'):
        return(Ori(binary))
    if(binary[:6]=='100011'):
        return(Lw(binary))
    if (binary[:6] == '101011'):
        return (Sw(binary))
    if (binary[:6]=='001111'):
        return (Lui(binary))
    if (binary[:6]=='001010'):
        return (Slti(binary))
    if (binary[:6]=='000100'):
        return (Beq(binary,i))
    if (binary[:6]=='000101'):
        return (Bne(binary,i))

def Jtype(binary):
    if (binary[:6]=="000010"):
        return (J(binary),1)
    if (binary[:6] == '000011'):
        return(Jal(binary),2)



#-------------------------------------------------------------------------------------------------



#R-------------------------------------------------
#TYPE----------------------------------------------
def Add(binary):
    return("Add "+Convert(binary[16:21])+Convert(binary[6:11])+Convert(binary[11:16]))

def Sub(binary):
    return("Sub "+Convert(binary[16:21])+Convert(binary[6:11])+Convert(binary[11:16]))

def And(binary):
    return("And "+Convert(binary[16:21])+Convert(binary[6:11])+Convert(binary[11:16]))

def Or(binary):
    return("Or " +Convert(binary[16:21])+Convert(binary[6:11])+Convert(binary[11:16]))

def Sll(binary):
    return ("Sll " + Convert(binary[16:21]) + Convert(binary[11:16])+str(int(binary[21:26],2)))

def Srl(binary):
    return ("Srl " + Convert(binary[16:21]) + Convert(binary[11:16])+str(int(binary[21:26],2)))

def Slt(binary):
    return ("Slt " + Convert(binary[16:21]) + Convert(binary[6:11]) + Convert(binary[11:16]))

def Jr(binary):
    return ("Jr " + Convert(binary[6:11]))


#I-------------------------------------------------
#TYPE----------------------------------------------
def Addi(binary):
    return ("Addi " + Convert(binary[11:16]) + Convert(binary[6:11])+str(int(binary[16:32],2)))

def Ori(binary):
    return ("Ori " + Convert(binary[11:16]) + Convert(binary[6:11])+str(int(binary[16:32],2)))

def Lw(binary):
    if 2<=(int(binary[6:11], 2))<=25:
        return ("Lw " + Convert(binary[11:16]) + str(int(binary[16:32], 2)) + "(" + (Convert(binary[6:11]))[:-1]+ ")")
    else:
        return ("Lw "+ Convert(binary[11:16]) + str(int(binary[16:32],2))+"("+(Convert(binary[6:11]))+")")

def Sw(binary):
    return ("Sw "+ Convert(binary[11:16]) + str(int(binary[16:32],2))+"("+(Convert(binary[6:11]))[:-1]+")")

def Lui(binary):
    return("Lui "+ Convert(binary[11:16])+ str(int(binary[16:32],2)) )

def Slti(binary):
    return ("Slti "+ Convert(binary[11:16]) + Convert(binary[6:11])+str(int(binary[16:32],2)))

def Beq(binary,current):
    newlocation=str(int(binary[16:32],2)+current+1)
    if 10000<(int(binary[16:32],2)):
        newlocation=str(current+1-(int(toTwosComplement(binary[16:32]),2)))

    location = current
    nametouse = "label" + str(newlocation)
    globals()[nametouse] = newlocation



    return ("Beq "+ Convert(binary[6:11])+ Convert(binary[11:16]) +"label"+newlocation)

def Bne(binary,current):
    newlocation=str(int(binary[16:32],2)+current+1)
    if 10000<(int(binary[16:32],2)):
        newlocation=str(current+1-(int(toTwosComplement(binary[16:32]),2)))

    location = current
    nametouse = "label" + str(newlocation)
    globals()[nametouse] = newlocation



    return ("Bne "+ Convert(binary[6:11])+ Convert(binary[11:16]) +"label"+newlocation)


#J-------------------------------------------------
#TYPE----------------------------------------------


def J(binary):
    location = int(binary[16:32], 2)
    return(location)

def Jal(binary):
    location = int(binary[16:32], 2)
    return(location)


#-------------------------------------------------------------------------------------------------


#Convert Function---------------------------------
def Convert(binary):
    dec=int(binary, 2)
    if (dec==0):
        result= ("$zero")

    elif (2<=dec<=3):
        value=dec-2
        result = ("$v" + str(value)+" ")

    elif (4<=dec<=7):
        value=dec-4
        result = ("$a" + str(value) + " ")


    elif (8<=dec<=15):
        value=dec-8
        result = ("$t" + str(value) + " ")

    elif (16<=dec<=23):
        value=dec-16
        result=("$s"+str(value)+" ")

    elif (24<=dec<=25):
        value=dec-16
        result = ("$t" + str(value) + " ")

    elif (dec==28):
        result = ("$gp")

    elif (dec==29):
        result = ("$sp")

    elif (dec== 30):
        result = ("$fp")

    elif (dec== 31):
        result = ("$ra")

    return(result)

#MAIN--------------------------------------------------------------------------------------------


#open the textfiel
with open("HexToDissemble.txt","r") as f:
    save=[line.rstrip('\n') for line in f]
    hex = open("step2.txt", "w").close()
    for i in range (0,filelen("HexToDissemble.txt")):
        write(save[i],i)
    #save the lines into step2
    hex = open("DissembledMips.txt", "w").close()
    with open("step2.txt", "r") as fi:
        save1 = [line.rstrip('\n') for line in fi]
        for j in range (0,filelen("step2.txt")):
            if("label"+str(j))in globals():
                save1[j] = ("label"+str(j) + ":  " + save1[j])
                hex = open("DissembledMips.txt", "a")
                hex.write(save1[j])
                hex.write("\n")
                hex.close()
            else:
                hex = open("DissembledMips.txt", "a")
                hex.write("         "+save1[j])
                hex.write("\n")
                hex.close()
    #insert result into dissembledmips
    import os
    #remove the temporary textfile
    os.remove("step2.txt")

