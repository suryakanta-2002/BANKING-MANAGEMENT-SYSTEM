#Depositcustomer.py <---module Name
import pickle
def withdraw():
    try:
        customeraccno=int(input("Enter Customer Account Number:"))
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
            print("No Customer Records Found ! try-Again")
            return
        except EOFError:
            print("File is Empty! No records Found Try-Again")
            return
        #updated balance if account is found
        found=False
        for record in records:
            if record[0]==customeraccno:
                wamt = float(input("Enter Withdraw Amount:"))
                if wamt > record[2]:
                    print("Insufficient Balance!  Available balance: {}".format(record[2]))
                    return
                record[2]-=wamt
                found=True
                print("Withdraw Successfully with Amount :{}".format(wamt))

                break
        if not found:
            print("Account Not Found try-Again")
            return
        #write updated records back to file
        with open("customerdata.txt", "wb") as fp:
            for rec in records:
                pickle.dump(rec, fp)
    except ValueError:
        print("Don't enter alnums,strs and symbols for Customer Account Number")