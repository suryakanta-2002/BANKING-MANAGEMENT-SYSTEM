#Depositcustomer.py <---module Name
import pickle
def deposit():
    try:
        customeraccno=int(input("Enter Customer Account Number:"))
        #amt=float(input("Enter Deposit Amount:"))
        records=[]
        #Try reading existing records
        try:
            with open("customerdata.txt", "rb") as fp:
                while True:
                    try:
                        record=pickle.load(fp)
                        records.append(record)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No Customer Records Found ! Try-Again")
            return
        except EOFError:
            print("File Is Empty! No Records Found Try-Again")
            return
        #updated balance if account is found
        found=False
        for record in records:
            if record[0]==customeraccno:
                amt = float(input("Enter Deposit Amount:"))
                record[2]+=amt
                found=True
                print("Deposit Successfully with Amount :{}".format(amt))
                break
        if not found:
            print("Account Not Found try-again")
            return
        #write updated records back to file
        with open("customerdata.txt", "wb") as fp:
            for rec in records:
                pickle.dump(rec, fp)
    except ValueError:
        print("Don't enter alnums,strs and symbols for Customer Account Number")

