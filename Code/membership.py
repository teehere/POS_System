import os
import Maintenance as main


def displayRec(rec):
    print("-"*50)
    for i in range(len(rec)):
        floatNum = main.isFloat(rec[i][2])
        if floatNum:
            print("%6s   %-22s   %8.2f"%(rec[i][0],rec[i][1],float(rec[i][2])))
        else:
            print("%-22s   %-10s   %s"%(rec[i][0],rec[i][1],rec[i][2]))
    print("-"*50)
    
def payMethod():
    print("-"*50)
    typeLst = ["  <P>remium","  <G>old   ","  <N>ormal "]
    payLst = ["<1> Cash","<2> Credit Card","<3> eWallet"]
##    i = 0
    print("  Types \t\t Payment Methods")
##    while i < len(typeLst and payLst):
##        print("%s \t\t %-10s"%(typeLst[i],payLst[i]))
##        i += 1

    for i in range(len(typeLst)):
        print("%s \t\t %-10s"%(typeLst[i],payLst[i]))
        
    print()
    print("NOTED: <C>heck to check the record!")
    print(" !ONLY AVALABLE AT THE MAIN MEMBERSHIP LOBBY! ")
    print("-"*50)

def premium():
    loop = True
    while loop:
        payLst = ["Cash","Credit Card","eWallet"]
        payment = input("Select Preferable Payment Method <Q>uit >> ").upper().strip()
        digit = main.isDigit(payment)
        if digit:
            os.system("cls")
            readM = main.readFile("member","r")
            displayRec(readM)
            if payment not in ['1','2','3']:
                loop = False
            else:
                name = input("Enter User Name <Q>uit >> ").upper().strip()
                if name == "Q":
                    print("-"*22,"Quit","-"*22)
                    loop = False
                    input()
                elif len(name) >= 1:
                    print("Discount offered will be 20%!")
                    getPay = payLst[int(payment)-1]
                    readM.append([name,"Premium",getPay])
                    readM = main.SaveFile("member","w",readM)
                    print("-"*20,"Recorded","-"*20)
                    loop = False
                    input()
                else:
                    print("-"*10,"Invalid Input, Pls Try Again","-"*10)
                    loop=False
                    input()
        elif payment == "Q":
            print("-"*12,"Quit to previous option","-"*13)
            loop = False
            input()
        else:
            print("-"*10,"Invalid Option, Pls Try Again","-"*10)
            loop = False
            input()

def gold():
    loop = True
    while loop:
        payLst = ["Cash","Credit Card","eWallet"]
        payment = input("Select Preferable Payment Method <Q>uit >> ").upper().strip()
        digit = main.isDigit(payment)
        if digit:
            os.system("cls")
            readM = main.readFile("member","r")
            displayRec(readM)
            if payment not in ['1','2','3']:
                loop = False
            else:
                name = input("Enter User Name <Q>uit >> ").upper().strip()
                if name == "Q":
                    print("-"*22,"Quit","-"*22)
                    loop = False
                    input()
                elif len(name) >= 1:
                    print("Discount offered will be 10%!")
                    getPay = payLst[int(payment)-1]
                    readM.append([name,"Gold",getPay])
                    readM = main.SaveFile("member","w",readM)
                    print("-"*20,"Recorded","-"*20)
                    loop = False
                    input()
                else:
                    print("-"*10,"Invalid Input, Pls Try Again","-"*10)
                    loop=False
                    input()
                    
        elif payment == "Q":
            print("-"*12,"Quit to previous option","-"*13)
            loop = False
            input()
        else:
            print("-"*10,"Invalid Option, Pls Try Again","-"*10)
            loop = False
            input()

def normal():
    loop = True
    while loop:
        payLst = ["Cash","Credit Card","eWallet"]
        payment = input("Select Preferable Payment Method <Q>uit >> ").upper().strip()
        digit = main.isDigit(payment)
        if digit:
            os.system("cls")
            readM = main.readFile("member","r")
            displayRec(readM)
            if payment not in ['1','2','3']:
                loop = False
            else:
                name = input("Enter User Name <Q>uit >> ").upper().strip()
                if name == "Q":
                    print("-"*22,"Quit","-"*22)
                    loop = False
                    input()
                elif len(name) >= 1:
                    print("Discount offered will be 5%!")
                    getPay = payLst[int(payment)-1]
                    readM.append([name,"Normal",getPay])
                    readM = main.SaveFile("member","w",readM)
                    print("-"*20,"Recorded","-"*20)
                    loop = False
                    input()
                else:
                    print("-"*10,"Invalid Input, Pls Try Again","-"*10)
                    loop=False
                    input()
                    
        elif payment == "Q":
            print("-"*12,"Quit to previous option","-"*13)
            loop = False
            input()
        else:
            print("-"*10,"Invalid Option, Pls Try Again","-"*10)
            loop = False
            input()

def Delete():
    readM = main.readFile("member","r")
    loop = True
    step = 1
    while loop:
        if step == 1:
            name = input("Enter User's Name  <Q>uit             >> ").upper().strip()
            check =  main.check(name,readM)
            if name == "Q":
                print("-"*12,"Quit To Previous Option","-"*13)
                loop = False
                input()
            elif check:
                step=step+1
            else:
                print("-"*5,"Item Does Not Exist, Cannot Be Deleted","-"*5)
        if step == 2:
            search = name
            for sublist in readM:
                if name in sublist:
                    readM.remove(sublist)
                    readM = main.SaveFile("member","w",readM)
                    print("-"*20,"Removed","-"*21)
            break
    return(readM)            

def Modify():
    readM = main.readFile("member","r")
    loop = True
    step = 1
    while loop:
        if step == 1:
            name = input("Enter User's Name to Modify    <Q>uit >> ").upper().strip()
            if name == "Q":
                print("-"*12,"Quit To Previous Option","-"*13)
                loop = False
                input()
            elif main.check(name,readM):
                step += 1
            else:
                print("-"*4,"Item Does Not Exist, Cannot Be Modified","-"*5)
        if step == 2:
            modifyWhat = input("\n<N>ame <T>ype <P>ayment Method <Q>uit >> ").upper().strip()
            if modifyWhat == "Q":
                print("-"*21,"Quit","-"*23)
                loop = False
                input()
            elif modifyWhat == "T":
                NewType = input("Enter New Type of Membership <Q>uit   >> ").upper().strip()
                typeLst = ["P","G","N"]
                if NewType =="Q":
                    print("-"*21,"Quit","-"*23)
                    input()
                elif NewType not in typeLst:
                    print("-"*10,"Invalid Option, Pls Try Again","-"*10)
                    input()
                else:
                    newT = {"P":"Premium","G":"Gold","N":"Normal"}
                    getNewT = newT[NewType]
                    search = name
                    for sublist in readM:
                        if name in sublist:
                            position = readM.index(sublist)
                            readM[position][1] = getNewT
                            readM = main.SaveFile("member","w",readM)
                            print("-"*5,"Successfully Modified Type of Membership","-"*5)
                            input()
                    break
            elif modifyWhat == "P":
                NewPay = input("Enter New Payment Method <Q>uit       >> ").upper().strip()
                payLst = ["1","2","3"]
                if NewPay == "Q":
                    print("-"*21,"Quit","-"*23)
                    loop = False
                    input()
                elif NewPay not in payLst:
                    print("-"*10,"Invalid Option, Pls Try Again","-"*10)
                    input()
                else:
                    newP = {"1":"Cash","2":"Credit Card","3":"eWallet"}
                    getNewP = newP[NewPay]
                    search = name
                    for sublist in readM:
                        if name in sublist:
                            position = readM.index(sublist)
                            readM[position][2] = getNewP
                            readM = main.SaveFile("member","w",readM)
                            print("-"*6,"Successfully Modified Payment Method","-"*7)
                            input()
                    break  
            elif modifyWhat=="N":
                NewName = input("Enter New User's Name <Q>uit          >> ").upper().strip()
                if NewName == "Q":
                    print("-"*21,"Quit","-"*23)
                    loop = False
                    input()
                elif main.check(NewName,readM):
                    print("-New User's Name same as Old User's Name, Pls Reenter-")
                else:
                    search = name
                    for sublist in readM:
                        if name in sublist:
                            position = readM.index(sublist)
                            readM[position][0] = NewName
                            readM = main.SaveFile("member","w",readM)
                            print("-"*8,"Successfully Modified User's Name","-"*8)
                            input()
                    break
            else:
                print("-"*9,"Invalid Option, Pls Try Again","-"*10)
                input()
                
    
    return(readM)

def check():
    loop = True
    while loop:
        os.system("cls")
        payMethod()
        readM = main.readFile("member","r")
        displayRec(readM)
        opt = input("<M>odify  <D>elete  <Q>uit            >> ").upper().strip()
        if opt == "Q":
            print("-"*13,"Quit to previous lobby","-"*13)
            input()
            loop = False
        elif opt == "M":
            Modify()
        elif opt == "D":
            Delete()
        else:
            print("-"*10,"Invalid Option, Pls Try Again","-"*10)
            input()

def memberM():
    loop = True
    while loop:
        os.system("cls")
        print("-"*50)
        print(" "*13,"Membership Maintanance"," "*13)
        payMethod()
        opt = input("Enter Type of Membership <C>/<Q>uit     >> ").upper().strip()
        if opt == "Q":
            print("-"*11,"Successfully Quit to Menu","-"*12)
            loop = False
        elif opt == "P":
            premium()
        elif opt == "G":
            gold()
        elif opt == "N":
            normal()
        elif opt == "C":
            check()
        else:
            print("-"*10,"Invalid Option, Pls Try Again","-"*10)
            input()
        
if __name__=="__main__":
    memberM()
       
