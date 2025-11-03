##ASSIGNMENT MENU
#menu() = displays menu page
#Opt = Option
#ItemMain() = Item Maintenance
#InvManag() = Inventory Management
#MemberM() = Member Maintenance
#Sales() = Sales
#Reports() = Reports

#file=assfile.txt

SPACE = 6
SPACE2 = 3

import os
import Maintenance as main
import membership as member
import StockManage as stock
import Sales as Sales
import report
    
def menu():
    loop = True
    while loop:
        os.system("cls")
        print("-"*50)
        print(" "*15,"ABC Retail Sdn Bhd"," "*15)
        print("-"*50) 
        print("<1> Item Maintenance")
        print("<2> Stock/inventory Management")
        print("<3> Membership Maintainence")
        print("<4> Sales")
        print("<5> Reports")
        print("<Q>uit")
        print("-"*50)
        Opt =(input ("Option >> ")).upper().strip()
        digit = main.isDigit(Opt)
        if digit:
            if Opt == "1":
                main.ItemMain()
                input()
            elif Opt == "2":
                stock.InvManag()
                input()
            elif Opt == "3":
                member.memberM()
                input()
            elif Opt == "4":
                Sales.sale()
                input()
            elif Opt == "5":
                report.report()
                input()
            else:
                print("-"*5,"Invalid Input","-"*15)
                input()
        elif Opt == "Q":
            print("-"*15,"Successfully Quit","-"*16)
            loop = False
            input()
        else:
            print("-"*10,"Invalid Input, Pls Try Again","-"*10)
            input()

if __name__ =="__main__":
    menu()
