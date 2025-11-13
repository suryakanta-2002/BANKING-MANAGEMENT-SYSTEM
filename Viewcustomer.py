#Viewcustomer.py <------Module Name
import pickle
def viewcustomer():
    try:
        with open("customerdata.txt","rb") as fp:
            records=[]   #empty list created for Holding records of file
            while(True):
                try:
                    record=pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
        #Get customer account number for view
        found=False
        customeraccno=int(input("Enter customer account number to view:"))
        for record in records:
            if (record[0]==customeraccno):
                rec=record
                found=True
                break
        print("-"*50)
        if (found):
            print("Customer Account Number:",rec[0])
            print("Customer Name:",rec[1])
            print("Customer Account Balance:",rec[2])
            print("Customer PIN:",rec[3])
        else:
            print("\t{} Customer Account number not found".format(customeraccno))
        print("-" * 50)
    except FileNotFoundError:
        print("File Not Found try-again")

def viewallcustomer():
    try:
        with open("customerdata.txt","rb") as fp:
            print("-" * 50)
            print("\tACC.NUMBER\tNAME\tBALANCE\tPIN")
            print("-" * 50)
            while(True):
                try:
                    record=pickle.load(fp)
                    for value in record:
                        print("\t{}".format(value),end="  ")
                    print()
                except EOFError:
                    print("-"*50)
                    break
    except FileNotFoundError:
        print("File Not Found try-again")