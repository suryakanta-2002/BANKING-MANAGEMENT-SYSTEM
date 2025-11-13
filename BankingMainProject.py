#BankingMainProject.py<-----Main Project
from BankingMenu import menu
from Addcustomer import addcustomer
from Viewcustomer import viewcustomer,viewallcustomer
from Searchcustomer import searchcustomer
from Depositcustomer import deposit
from Withdrawcustomer import withdraw
from Deletecustomer import deletecustomer
from customerPinupdate import updatepin
from Generatepin import generatepin
while(True):
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                addcustomer()
            case 2:
                deletecustomer()
            case 3:
                deposit()
            case 4:
                withdraw()
            case 5:
                viewcustomer()
            case 6:
                viewallcustomer()
            case 7:
                searchcustomer()
            case 8:
                updatepin()
            case 9:
                generatepin()
            case 10:
                print("\tThanks for using this Bank")
                break
            case _:
                print("\tYour selection of operation is wrong-try again")
    except ValueError:
        print("\tDont Enter alnums,strs and Symbols for choice-try again")