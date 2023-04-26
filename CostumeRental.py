import Functions
print("\n")
Functions.datetime_ontop()
Functions.welcome()
while(True):
    print("Here are the options for your choices:")
    Functions.show_options()
    try:
        user_choice=int(input("Enter the option that you want: "))
        if user_choice<=0:
                print("Please enter the valid option..")
        elif user_choice>4:
                print("Please Enter a valid option..")
        print("\n")
    except:
        print("Invalid option please choose again")
        continue
    
    if user_choice == 1: 
        a=Functions.display_keyvalue_in_dict()
        Functions.display_in_tabularform(a)
        print("\n")
    elif user_choice == 2:
        a=Functions.display_keyvalue_in_dict()
        Functions.user_input_forRent()
        callagain=True
        while callagain:
            Functions.display_in_tabularform(a)
            b=Functions.rent_costume(a)
            Functions.for_change_inrent(b) 
            Functions.for_invoice_inrent(a) 
            rentAgain=input("Do you want to rent Again? Enter 'yes' for rent and 'No' for Exit: ")
            print("\n")
            if rentAgain.isalpha():
                if rentAgain.lower()=='y' or rentAgain.lower()=='yes':
                    callagain=True
                elif rentAgain.lower()=='n'or rentAgain.lower()== 'no':
                    Functions.thank_you()
                    callagain=False
                    print("Thank you for visiting with us.")
                    print("\n")
                else:
                    print("Enter a valid data..")
        
    elif(user_choice==3):
        a=Functions.display_keyvalue_in_dict()
        Functions.user_input_forreturn()
        callagain=True
        while callagain:
            Functions.display_in_tabularform(a)
            b=Functions.return_costume(a)
            c=Functions.for_changein_Return(b) 
            Functions.for_invoice_inReturn(b) 
            renturnAgain=input("Do you want to renturn Again? Enter 'yes' for rent and 'No' for Exit: ")
            print("\n")
            if renturnAgain.isalpha():
                if renturnAgain.lower()=='y' or renturnAgain.lower()=='yes':
                    callagain=True
                elif renturnAgain.lower()=='n'or renturnAgain.lower()== 'no':
                    Functions.thank_you2()
                    callagain=False
                    print("Thank you for visiting with us.")
                    print("\n")
                else:
                    print("Enter a valid data..")
    elif (user_choice==4):
        break
    
        


        
