from datetime import datetime
f_name="set.txt"

#function for datetime_ontop
def datetime_ontop():
    global rent_date
    global return_date
    from datetime import datetime
    from datetime import date   
    return_date=str(date.today())
    rent_date=str(date.today())
    now=(datetime.now())

    # convert time into string
    current_time=now.strftime("%H:%M:%S")
    if(current_time<"%H:%M:%S"):
        print("\t\t    Hello! Good Morning")
    elif (current_time>"%H:%M:%S"):
        print("\t\t    Hello! Good Afternoon") 
# function for welcome message 
def welcome():
    print(""" 
    ******************************************************
    ************Welcome To Costume Rental Shop************
    **************Availiable for you to rent**************
    ***************Itahari-4, Sunsari,Nepal***************
    ******************************************************
    """)
#function for show_options
def show_options():
    print("1. Display Details...")
    print("2. Rent costumes...")
    print("3. Return costumes...")
    print("4. Exit")

#functions for display_keyvalue_in_dict
def display_keyvalue_in_dict():
    # file open in read mode and put on file variable
    file=open(f_name, "r")
    shop_dict={}
    id=1
    # use for each loop in file
    for key_value in file:
        shop_dict[id]=key_value.replace("\n","").split(",")
        id+=1
    return shop_dict
#functions for display_in_tabularform
def display_in_tabularform(shop_dict):
    print("Id\t\tName\t\t\tBrand\t\t\tPrice\t\tQuantity")
    print("\n")
    # use for each loop in shop_dict
    for key, values in shop_dict.items():
        print(key, end="\t\t")
        for val in values:
            print(val, end="\t\t")
        print("\n")
#functions for user_input_forRent
def user_input_forRent():
    check=True
    while check:
        global cus_Name
        cus_Name = input("Enter the name of customer:  ")
        print("\n")
        if cus_Name.isdigit():
            print("Customer name must not contains decimal please enter a valid name..")
        elif cus_Name.isdecimal():
            print("customer name must not contains positive or negative number..")
        print("\n")
        # check=True
        customerName=cus_Name.replace(" ", "")
        if customerName.isalpha():
            check=False
            #keep cus_Name in file and text file generate
            file=cus_Name + ".txt"
            #file open as write mode
            with open(file, "w") as filewrite:
                filewrite.write("""
                --------------Imagine Costume Rental Shop-------------
                ---------------Itahari-4, Sunsari,Nepal---------------
                """)
                # print cus_Name and rent_date
                filewrite.write("\nCustomer Name: " + cus_Name + "                                           Date: " + rent_date + " \n\n")
                filewrite.write("Name\t\t\t\tBrand\t\t\tPrice\t\t\tQuantity\t\t\tTotal\n\n")

def rent_costume(shop_dict):
    again=True
    while again:
        global id    
        id=int(input("Enter the costume Id you want to rent: "))
        print("\n")
        if id<=0:
            print("Please enter the valid Id..")
        elif id>4:
            print("Please Enter a valid Id..")
            # continue
            # Use for each loop in shop_dict
        for key,values in shop_dict.items():
                loop=False
                if id==key:
                    check=True
                    while check:
                        global quantity
                        try:
                            quantity=int(input("Enter the quantity you want to rent: "))
                            print("\n")
                            qua_item=int(values[3])    
                            if(quantity>qua_item):
                                print("Sorry not availiable")
                                check=True
                                continue    
                            elif qua_item>=quantity:
                            #access the value of all key quantities in check_qua variable
                                check_qua=int(shop_dict[key][3])
                                check_qua -= quantity
                                shop_dict[key][3]=check_qua
                                print("Rented sucessfully")
                                print("\n")
                                check=False
                                again=False
                        except:
                            print("Invalid Quantity Enter..")  
                            check=True      
    return shop_dict
# Function for for_change_inrent
def for_change_inrent(shop_dict):
    file="set.txt"
    #open file as write mode as in a
    with open(file,"w") as a:
        for value in shop_dict.values():
            for i in range(len(value)):
                if i==3:
                    # if 3 index start, then replace by \n
                    a.write(str(value[i])+"\n")
                else:
                    a.write(str(value[i])+",")
grand=0      
# function for for_invoice_inrent            
def for_invoice_inrent(shop_dict):
    file=cus_Name + ".txt"
    #open file as a+ for invoice
    with open(file, "a+") as filewrite:
        value=shop_dict[id]
        Name=value[0]
        Brand=value[1]
        Price=str(value[2])
        Price_=Price.replace("$","")    
        Quantity=str(quantity) 
        Total=str(float(Price_)*quantity)
        global grand
        grand=grand+float(Total)
        filewrite.write(Name + "\t\t" + Brand + "\t\t" + Price_ + "\t\t\t\t\t" + Quantity + "\t\t\t\t" + Total + "\n")
# function for thank_you message
def thank_you():
    file=cus_Name + ".txt"
    with open(file, "a+") as filewrite:
        global grand
        G_total=str(grand)
        filewrite.write("\n\n\n\n\n\n")
        filewrite.write("                                                                  Grand Total: "+G_total)
        filewrite.write("\n\n\n")
        filewrite.write("\t\t\t\t\t\t\t\t Thank you for renting with us.")
        grand=0
        

#function for user_input_forreturn
def user_input_forreturn():
    global cusName
    cusName = input("Enter the name of customer:  ")
    print("\n")
    if cusName.isdigit():
        print("Customer name must not contains decimal please enter a valid name..")
    elif cusName.isdecimal():
        print("customer name must not contains positive or negative number..")
    print("\n")
    customer_Name=cusName.replace(" ", "")
    if customer_Name.isalpha():
        file=cusName+".txt"
        # open file as a write mode
        with open(file, "w") as filewrite:
            filewrite.write("""
            --------------Imagine Costume Rental Shop-------------
            ---------------Itahari-4, Sunsari,Nepal---------------
            """)

            filewrite.write("\nCustomer Name: " + cusName + "                                           Date: " + return_date + " \n\n")
            filewrite.write("Name\t\t\t\tBrand\t\t\tPrice\t\t\tQuantity\t\t\tTotal\n\n")
    loop =True
    while loop:
        global day
        input_Rentdate=input("Enter the rented date in yy-mm-dd format: ")
        print("\n")
        yy,mm,dd=input_Rentdate.split("-")
        Year=int(yy)
        Month=int(mm)
        Day=int(dd)
        if Year>2022 and Month>13 and Day>31:
            print("Invalid date")
        elif Year>2022:
            print("Invalid year")
        elif Month>13:
            print("Invalid months")
        elif Day>32:
            print("Invalid day")
        else:
            loop=False
            rented_date=datetime.strptime(input_Rentdate, "%Y-%m-%d")
            returned_date=datetime.strptime(return_date, "%Y-%m-%d")
            sub=returned_date-rented_date
            day=sub.days
            if day<0:
                print("Please input valid date")
                loop=True
    


# functions for return_costume


def return_costume(shop_dict):
    returned=True
    while returned:
        try:
            global id
            id=int(input("Enter the costume Id you want to renturn: "))
            for key, values in shop_dict.items():
                if key == id:
                    noError=True
                    while noError:
                        global quantity
                        try:         
                            quantity=int(input("Enter the quantity you want to return: "))
                            check_qua=int(shop_dict[key][3])
                            check_qua += quantity
                            shop_dict[key][3]=check_qua
                            print("Returned sucessfully")
                            print("\n")
                            returned=False
                            noError=False
                        except:
                            print("Enter valid quantity")
                            noError=True
        except:
            print("Input valid id")
            returned=True
    # print(shop_dict)
    return shop_dict
                    
# funciton for for_changein_Return            
def for_changein_Return(shop_dict):
    file="set.txt"
    #open file as a write mode
    with open(file,"w") as a:
        for value in shop_dict.values():
            for i in range(len(value)):
                if i==3:
                    a.write(str(value[i])+"\n")
                else:
                    a.write(str(value[i])+",")
# functions for for_invoice_inReturn
grand_=0

def for_invoice_inReturn(shop_dict):
    file=cusName+".txt"
    with open(file, "a+") as filewrite:
        value=shop_dict[id]
        Name=value[0]
        Brand=value[1]
        Price=str(value[2])
        Price_=Price.replace("$","")
        Quantity=str(quantity)
        Total=str(float(Price_)*quantity)
        global grand_
        grand_=grand_+float(Total)
        filewrite.write(Name + "\t\t" + Brand + "\t\t" + Price_ + "\t\t\t\t\t" + Quantity + "\t\t\t\t" + Total + "\n")

def thank_you2():
    global grand_
    if day<5:
        new=str(grand_)
        file=cusName + ".txt"
        with open(file, "a+") as filewrite:
            filewrite.write("\n")
            filewrite.write("                                                           Grand Total: "+new)
            filewrite.write("\n")
            filewrite.write("\t\t\t\t\t\t\t Thank you for returning.") 
            grand_=0
    else:
        extra_date=day-5
        extra_charge=3
        charge_=extra_charge*extra_date
        charge_amount=str(charge_)
        file=cusName + ".txt"
        with open(file, "a+") as filewrite:
            # global grand_
            grand_=grand_+charge_
            new=str(grand_)
            filewrite.write("\n")
            filewrite.write("                                                           Extra Charge: "+charge_amount)
            filewrite.write("\n")
            filewrite.write("                                                           Total Charge: "+new)
            filewrite.write("\n")
            filewrite.write("\t\t\t\t\t\t\t Thank you for returning.") 
            grand_=0
