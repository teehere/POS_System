#Program name :Main.py
#created by   :JY
#created      :07/11/2023
#import       :POSvalid
#             :L4

import os

def openFile(filename,mode) :
    f=open(filename+".txt",mode)
    recLst=f.readlines()#read entire file and store in a list
    f.close()
    lst=[]
    for i in range(len(recLst)):
        trec=recLst[i].strip("\n").split("|")
        lst.append(trec)
    return lst

def readFile(filename,mode):
    f=open(filename+".txt",mode)
    rec=f.readlines()
    f.close()
    recf=[x.strip("\n").split("|") for x in rec]
    return recf

def SaveFile(filename,mode,recf):
    wStr=""
    for i in range(len(recf)):
        wStr+="|".join(recf[i])+"\n"
    f=open(filename+".txt",mode)
    f.write(wStr)
    f.close()

def displayRec(recf):
    print("-"*50)
    for i in range(len(recf)):
        print("%6s   %-22s   %8.2f"%(recf[i][0],recf[i][1],float(recf[i][2])))
    print("-"*50)

def check(ItemCode,recf):
    status=False
    for i in range(len(recf)):
        if ItemCode == recf[i][0]:
            status=True
            break
    return status

def isDigit(num):
    status=True
    try:
        num=int(num)
    except:
        status=False
    return status

def isFloat(num):
    status=True
    try:
        num=float(num)
    except:
        status=False
    return status


def Add(opt,recf):
    rec=readFile("assfile","r")
    loop=True
    step=1
    while loop:
        if step==1:
            ItemCode=input("Enter Item Code  <Q>uit             >> ").upper().strip()
            if ItemCode=="Q":
                loop=False
            elif check(ItemCode,rec):
                print("-"*6,"Item Exist, Please Add Another Item","-"*7)

            elif len(ItemCode)!=5:
                print("-"*2,"Invalid Input, Please Enter a FIVE Word Code","-"*2)
            else:
                step += 1
        if step == 2:
            ItemDesc=input("Enter Item Description  <Q>uit      >> ").upper().strip()
            if ItemDesc=="Q":
                loop=False
            else:
                step=step+1
        if step == 3:
            ItemPrice=input("Enter Item Price  <Q>uit            >> ").upper().strip()
            if ItemPrice == "Q":
                loop=False
            elif not isFloat(ItemPrice):
                print("-"*10,"Please Input Valid Price Value","-"*10)
            else:
                step=step+1
        if step == 4:
            rec.append([ItemCode,ItemDesc,ItemPrice,"0"])
            print("-"*10,"Item Added Successful","-"*10)
            loop=False
            
    SaveFile("assfile","w",rec)       
    return rec
    
    

def ItemMain():
    rec=readFile("assfile","r")
    loop=True
    while loop:
        os.system("cls")
        print("-"*50)
        print(" "*13,"Item Master Maintenance"," "*13)
        displayRec(rec)
        print("<A>dd <M>odify <D>elete \t\t<Q>uit")
        print("-"*50)
        opt=input("Enter Option                        >> ").upper().strip()
        if opt=="Q":
            print("-"*11,"Successfully Quit To Menu","-"*12)
            loop=False
        elif opt=="A":
            rec=Add(opt,rec)                    
        elif opt=="M":
            rec=Modify()   
        elif opt=="D":
            rec=Delete()       
        else:
            print("-"*9,"Invalid Option, Pls Try Again","-"*10)
            input()
        


             

    
def Modify():
    rec=readFile("assfile","r")
    loop=True
    step=1
    while loop:
        if step==1:
            ItemCode=input("Enter Item Code <Q>uit              >> ").upper().strip()
            if ItemCode=="Q":
                loop=False
            elif check(ItemCode,rec):
                step +=1
            else:
                print("-"*4,"Item Does Not Exist, Cannot Be Modified","-"*5)
        if step==2:
            modifyWhat=input("<C>ode <D>escription <P>rice <Q>uit >> ").upper().strip()
            if modifyWhat=="Q":
                loop=False
            elif modifyWhat=="D":
                NewDesc=input("Enter New Item Description <Q>uit   >> ").upper().strip()
                if NewDesc =="Q":
                    loop=False
                else:
                    search=ItemCode
                    for sublist in rec:
                        if ItemCode in sublist:
                            position=rec.index(sublist)
                            rec[position][1]=NewDesc
                    break
            elif modifyWhat=="P":
                NewPrice=input("Enter New Item Price <Q>uit        >> ").strip()
                if NewPrice =="Q":
                    loop=False
                elif not isFloat(NewPrice):
                    print("Please Input Valid Price Value")
                else:
                    search=ItemCode
                    for sublist in rec:
                        if ItemCode in sublist:
                            position=rec.index(sublist)
                            rec[position][2]=NewPrice
                    break  
            elif modifyWhat=="C":
                NewCode=input("Enter New Item Code <Q>uit          >> ").upper().strip()
                if NewCode=="Q":
                    loop=False
                elif len(NewCode)!=5:
                    print("-"*2,"Invalid Input, Please Enter a FIVE Word Code","-"*2)
                elif check(NewCode,rec):
                    print("- New Item Code same as Old Item Code, Please Reenter -")
                else:
                    search=ItemCode
                    for sublist in rec:
                        if ItemCode in sublist:
                            position=rec.index(sublist)
                            rec[position][0]=NewCode
                    break  
            else:
                print("-"*10,"Invalid Option, Pls Try Again","-"*10)
                input()
                
                
    SaveFile("assfile","w",rec)
    return(rec)
    
    
    




def Delete():
    rec=readFile("assfile","r")
    loop=True
    step=1
    while loop:
        if step==1:
            ItemCode=input("Enter Item Code  <Q>uit             >> ").upper().strip()
            if ItemCode=="Q":
                loop=False
            elif len(ItemCode)!=5:
                print("-"*2,"Invalid Input, Please Enter a FIVE Word Code","-"*2)
            elif check(ItemCode,rec):
                step=step+1
            else:
                print("-"*5,"Item Does Not Exist, Cannot Be Deleted","-"*5)
        if step==2:
            search=ItemCode
            for sublist in rec:
                if ItemCode in sublist:
                    rec.remove(sublist)
            break
                
         
    SaveFile("assfile","w",rec)
    return(rec)
    

if __name__ =="__main__":
    ItemMain()



    
