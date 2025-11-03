#Sales
import datetime
import os
import StockManage
import Maintenance as main
recf=main.readFile("assfile","r")
membRec=main.readFile("member","r")


def displayRec(recf):
    print("-"*50)
    for line in recf:
        print("%6s   %-22s   %8.2f"%(line[0],line[1],float(line[2])))
    print("-"*50)

date = datetime.datetime.now()
def time():
    print("-" * 60)
    print("Sales Transaction Menu - - >   Date:", date.strftime("%D"), "Time:", date.strftime("%T"))
    print("-" * 60)

def pTime():
    print("-" * 50)
    print("Payment - - >   Date:", date.strftime("%D"), "Time:", date.strftime("%T"))
    print("-" * 50)

def get_item_details(item_code, recf):
    for item in recf:
        if item_code == item[0]:
            Desc=item[1]
            Price=float(item[2])
            current_stock=int(item[3])
            

    return Desc, Price,current_stock

getDisC=[]
def save_receipt(item_code, item_name, item_price, quantity, total_price, adj_amt, rounded, getDisC):
    itemSold = main.readFile("itemSold", "r")
    with open("receipt.txt", "a") as file:
        for i, item in enumerate(itemSold):
            #Check if the index is within the range of getDisC
            if i < len(getDisC):
                #Use the corresponding discount
                discount = getDisC[i]
            else:
                #If out of range, use the last available discount
                discount = getDisC[-1]
            file.write(f"{item[0]}|{item[1]}|{item[3]}|{item[2]}|{item[4]}|{float(discount):.2f}\n")

def discount(membRec):
    name = input("Please Enter Name >>").upper().strip()
    for item in membRec:
        if name == item[0].split("|")[0].strip():
            print("Match found!")
            if item[1] == "Gold":
                print("Membership is Gold")
                return 0.3 #30%
            elif item[1] == "Premium":
                print("Membership is Premium")
                return 0.25  #25%
            elif item[1] == "Normal":
                print("Membership is Normal")
                return 0.1  #10%
    print("Member Not Found")
    return 0.0

def receipt(item_code, quantity, recf, membRec):
    os.system("cls")
    pTime()

    for item in recf:
        if item_code == item[0]:
            memb = input("Any Membership?  <Y>ES  <Any Input For NO> >>").upper().strip()
            if memb=="Y":
                disc = discount(membRec)
                getDisC.append(disc)
            else:
                disc = 0.0
                getDisC.append(disc)
                
            itemSold=main.readFile("itemSold","r")
            prices=[]
            os.system("cls")
            print("Item\t\tQuantity\tPrice\tTotal Price")
            for i in range(len(itemSold)):
                price=float(itemSold[i][4])
                prices.append(price)
            total_price=sum(prices[:])
            
            displaysold(itemSold)    
            total_price = round(total_price, 2)
            disC=round((total_price*disc),2)
            print("Total(RM)\t\t\t                ", f"{total_price:10.2f}")
            total_price_after_dis = total_price-(disC)
            print("Discount(RM)\t\t\t\t\t",f"{(total_price*disc):10.2f}")
            print("Total After Discount(RM)\t\t\t", f"{total_price_after_dis:10.2f}")
            rounded = round(total_price_after_dis / 0.05) * 0.05
            sort = [total_price_after_dis, rounded]
            adj_amt = max(sort) - min(sort)
            print("Adjusted Amount (RM)\t\t\t\t", f"{adj_amt:10.2f}")
            rounded = round(rounded, 2)
            print("Payment paid(RM)\t\t\t\t", f"{rounded:10.2f}")
            print("=" * 50)

            save_receipt(item_code, item[1], item[2], quantity, total_price, adj_amt, rounded, getDisC)

            break

def displaysold(itemSold):
    print("-"*60)
    for line in itemSold:
        print("%5s    %22s   %-6s    %.2f   %8.2f"%(line[0],line[1],line[2],float(line[3]),float(line[4])))
    print("-"*60)
    
def update_stock(item_code, quantity, Stk):
    itemSold=main.readFile("itemSold","r")
    recf=main.readFile("assfile","r")
    for sold in itemSold:
        for item in recf:
            if sold[0] in item:
                position =recf.index(item)
                updateStk=int(recf[position][3])-int(sold[2])
                recf[position][3]=str(updateStk)
                main.SaveFile("assfile","w",recf)     
                break

    return recf


def payment(item_code, quantity, recf, membRec):
    itemSold=main.readFile("itemSold","r")
    loop=True
    while loop:
        os.system("cls")
        time()
        print("Item\t\t\tQuantity\tPrice\tTotal Price")
        displaysold(itemSold)
        pay = input("Proceed to Payment <P>ayment  <Q>uit: ").upper().strip()
        if pay == "P":
            receipt(item_code, quantity, recf,membRec)
            update_stock(item_code, quantity, recf)
            loop=False
        elif pay == "Q":
            print("-"*21,"Successfully Quit","-"*20)
            loop=False
        else:
            print("-"*23,"Invalid Input","-"*22)



def sell_items(recf, membRec):
    print(" "*16,"Chosen Items")
    print("-"*50)
    itemSold = []
    loop=True
    step=1
    while loop:
        if step==1:
            item_code = input("Enter Item Code   <Q>uit: ").upper().strip()
            if item_code == "Q":
                print("-" * 21, "Successfully Quit", "-" * 20)
                input()
                loop=False
            elif main.check(item_code, recf):##1 pass 1 no pass also consider pass...
                step+=1
            else:
                print("-" * 7, "Invalid Input, Please Enter a Valid Item Code", "-" * 6)
        if step==2:
            quantity = input("Enter Quantity   <B>ack  <Q>uit: ").upper().strip()
            if quantity == "Q":
                print("-" * 21, "Successfully Quit", "-" * 20)
                loop=False
            elif quantity == "B":
                step-=1  # Go back to entering the item code
            elif main.isDigit(quantity)and int(quantity)!=0:
                Desc, price,current_stock= get_item_details(item_code, recf)
                if int(quantity)>current_stock:
                    print("-" * 3, "Insufficient stock! Enter a valid quantity.", "-" * 3)
                else:
                    total_price = int(quantity) * price
                    itemSold.append([item_code,Desc,quantity,str(price),str(total_price)])
                    main.SaveFile("itemSold","w",itemSold)
                    step+=1
            else:
                print("----Invalid Quantity, Please Enter a Non-negative Number----")
        if step==3:
            itemSold=main.readFile("itemSold","r")
##            time()
##            displayRec(recf)
##            print(" "*16,"Chosen Items")
##            print("-"*50)
            os.system("cls")
            time()
            displayRec(recf)
            print(" "*16,"Chosen Items")
##            print("="*60)
            displaysold(itemSold)
            
            conf = input("<C>onfirm & Save <A>dd  <M>odify <D>elete  <Q>uit  >>").upper().strip()
            if conf == "C":
                payment(item_code, quantity, recf, membRec)
                loop=False
            elif conf == "A":
                step-=2
            elif conf == "M":
                step+=1
            elif conf == "D":
                step += 2
            elif conf == "Q":
                print("-" * 21, "Successfully Quit", "-" * 20)
                loop=False
            else:
                print("-" * 23, "Invalid Input", "-" * 22)


        if step==4:
            itemSold=main.readFile("itemSold","r")
            modify=input("Enter Code To Modify  <Q>uit >> ").upper().strip()
            if modify =="Q":
                loop=False
            else:
                for item in itemSold:
                    if modify in item:
                        newQ=input("New Quantity <Q>uit :" )
                        if newQ =="Q":
                            loop=False
                        else:
                            position=itemSold.index(item)
                            itemSold[position][2]=newQ
                            price=float(itemSold[position][3])
                            itemSold[position][4]=str(price*int(newQ))
                            main.SaveFile("itemSold","w",itemSold)
                            step-=1
                            break
                    if not main.check(modify,itemSold):
                        print("Item not found, Pls Try Again")
                        input()
                        

                
        if step ==5:
             delete=input("Enter Code To Delete   <Q>uit >> ").upper().strip()
             if delete =="Q":
                loop=False
             else:
                for item in itemSold:
                    if delete in item:
                            itemSold.remove(item)
                            itemSold=main.SaveFile("itemSold","w",itemSold)
                            step-=2
                            break
                    if not main.check(delete, itemSold):
                        print("-"*16,"No Item Found, Pls Try Again","-"*15)
                        input()
            
    return(itemSold)                


##def Clear(filename,mode,recLst):
##    wStr=""
##    f=open(filename+".txt",mode)
##    f.write(wStr)
##    f.close()
    
               
def sale():
    os.system("cls")
    time()
    recf = main.readFile("assfile", "r")
    displayRec(recf)
    membRec=main.readFile("member","r")
    loop = True
    sell_items(recf,membRec)

if __name__ == "__main__":
    sale()




        
