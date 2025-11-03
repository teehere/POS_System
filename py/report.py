#report

import os
import Maintenance as main

def displaySales():
    os.system("cls")
    rec=main.readFile("receipt","r")
    print("-"*117)
    print("Items\t\t\tPrice\t\tQuantity\tTotal Price\tDiscount\tAdjustment\tTotal Amount")
    print("-"*117)
    total=0
    totalP=0
    disC=0
    sales=[]
    #getItem=[]
    for line in rec:
        print(f"{line[1]}{"\t"}{float(line[2]):.2f} {"\t\t"} {int(line[3]):02d}{"\t\t"}{float(line[4]):7.2f}{"\t\t"}{float(line[-1]):6.2f}{"\t\t"}{float(line[5]):5.2f}{"\t\t"}{float(line[-2]):6.2f}")
        total += float(line[2])
        totalP += float(line[-2])
        disC += float(line[-1])
        sales.append([line[1],int(line[3])])
        #getItem.append(line[0])
    print("="*117)
    print(f"TOTAL SALES (RM){"\t\t\t\t\t\t\t\t\t\t\t "}{totalP:.2f}")
    print()

    loop=True
    while loop:
        recf=main.readFile("assfile","r")
        analyze=input("<A>nalyze the Data Above <Q>uit   >> ").upper().strip()
        if analyze == "Q":
            print("-"*38,"Successfully Quit To Report Maintanence","-"*38)
            loop=False
        elif analyze == "A":
            arrange=[[x[1],x[0]] for x in sales]
            sort=[x for x in arrange]
            sort.sort(reverse=True)
            profit=totalP-total
            print()
            print("-"*53,"ANALYSING","-"*54)
            print()
            print(f"The Best Selling Product          >> {sort[0][1]} ({sort[0][0]})")
            print(f"The Worst Selling Product         >> {sort[-1][1]} ({sort[-1][0]})")
            print(f"Total Discount                    >> {disC:.2f}")
            print(f"Profit Earned (RM)                >> {profit:.2f}")
            print()
            print("-"*53,"ANALYSING","-"*54)
            break
        else:
            print("-"*43,"Invalid Option, Pls Try Again","-"*43)
        break
  
def report():
    loop=True
    while loop:
        os.system("cls")
        print("-"*50)
        print(" "*21,"Report")
        print("-"*50)
        print("<1> Check Sales")
        print("-"*50)
        opt=input("Enter Option <Q>uit >> ").upper().strip()
        if opt == "Q":
            print("-"*11,"Successfully Quit To Menu","-"*12)
            loop=False
            input()
        elif opt == "1":
            displaySales()
            input()
        else:
            print("-"*9,"Invalid Option, Pls Try Again","-"*10)
            input()

if __name__=="__main__":
    report()
