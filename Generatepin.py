#Generatepin.py  <---Module Name
import pickle
import random
def generatepin():
    try:
        customeraccno=int(input("Enter the customer account number: "))
        #Load existing records
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
            print("No customer records found! please Try-again")
            return
        except EOFError:
            print("File is empty! No records found")
            return
        found=False
        for record in records:
            if record[0]==customeraccno:
                #Generate random 4-Digit Pin
                newpin=str(random.randint(1000,9999))
                record[3]=newpin
                found=True
                print("New PIN Generated Successfully for Account Number {}".format(record[0]))
                print("Your new PIN is: {}".format(newpin))
                break
        if not found:
            print("Account Not Found Please Try-Again")
        #write updated data back to file
        with open("customerdata.txt","wb") as fp:
            for rec in records:
                pickle.dump(rec,fp)
    except ValueError:
        print("Dont Enter Invalid input Please Enter a valid Numbers Try-Again")


