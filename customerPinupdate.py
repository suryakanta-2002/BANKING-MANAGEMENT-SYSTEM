#customerPinupdate.py  <---module Name
import pickle
def updatepin():
    try:
        customeraccno=int(input("Enter Customer Account Number: "))
        #Load all records first
        records=[]
        try:
            with open("customerdata.txt","rb") as fp:
                while True:
                    try:
                        record=pickle.load(fp)
                        records.append(record)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No customer records found! Please Try-Again")
            return
        except EOFError:
            print(" File is empty! No records available.")
            return
        found=False
        for record in records:
            if record[0]==customeraccno:
                print("Account Found for Customer Account Number: ",customeraccno)
                #Ask for new pin and confirmation
                while True:
                    newpin=input("Enter New 4-Digit PIN: ")
                    confirmpin=input("Confirm New PIN:")
                    if newpin==confirmpin and newpin.isdigit() and len(newpin)==4:
                        record[3]=newpin
                        found=True
                        print("PIN Updated Successfully")
                        break
                    else:
                        print("Invalid Or Mismatched PIN! try-again")
                break
        if not found:
            print("Account Not Found! Please Try-Again")
        #Write all records back to the file
        with open("customerdata.txt","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
    except ValueError:
        print("Don't enter alnums,strs and symbols for Customer Account Number")

