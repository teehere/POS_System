# Stock
import Maintenance as main
import os


def displayStk(Stk):
    print("-"*50)
    for i in range(len(Stk)):
        print("%6s\t%-22s\t\t%8s"%(Stk[i][0],Stk[i][1],(Stk[i][3])))
    print("-"*50)


def stockAlert():
    Stk=main.readFile("assfile","r")
    for i in range(len(Stk)):
        if int(Stk[i][3])<=10:
            print("LOW STOCK LEVEL:",Stk[i][1],"remaining stock",Stk[i][3])
    print()

def ModifyStk():
    Stk=main.readFile("assfile","r")
    loop=True
    step=1
    while loop:
        if step==1:
            ItemCode=input("Enter Item Code  <Q>uit             >> ").upper().strip()
            if ItemCode=="Q":
                loop=False
            elif main.check(ItemCode,Stk):
                step +=1
            else:
                print("-"*5,"Item Does Not Exist, Cannot Be Modified","-"*5)
        if step==2:
            modifyWhat=input("<S>tock <Q>uit >> ").upper().strip()
            if modifyWhat=="Q":
                loop=False
            
            elif modifyWhat=="S":
                NewStock=input("Enter New Stock <Q>uit              >> ").strip()
                if NewStock =="Q":
                    loop=False
                elif not main.isDigit(NewStock):
                    print("-"*5,"Please Input Integer Quantity of Stock","-"*5)
                else:
                    search=ItemCode
                    for sublist in range(len(Stk)):
                        if ItemCode in Stk[sublist]:
                            position=Stk.index(Stk[sublist])
                            Stk[position][3]=NewStock
                    break
            
            else:
                print("-"*9,"Invalid Option, Pls Try Again","-"*10)
                input()
    main.SaveFile("assfile","w",Stk)
    return Stk



def InvManag():
    loop=True
    Stk=main.readFile("assfile","r")
    while loop:
        os.system("cls")
        print("-"*50)
        print(" "*12,"Stock Master Maintanance"," "*13)
        displayStk(Stk)
        print("<M>odify\t\t\t\t<Q>uit")
        print("-"*50)
        stockAlert()
        opt=input("Enter Option <Q>uit                 >> ").upper().strip()
        if opt=="Q":
            print("-"*11,"Successfully Quit to Menu","-"*12)
            loop=False
        elif opt=="M":
            Stk=ModifyStk()
        else:
            print("-"*10,"Invalid Option, Pls Try Again","-"*10)
            input()

if __name__ =="__main__":
    InvManag()
