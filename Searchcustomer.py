#Searchcustomer.py  <------Module name
import pickle
def searchcustomer():
    with open("customerdata.txt","rb") as fp:
        records=[]   #empty list created for Holding records of file
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Get emp number from user
    found=False
    customeraccno=int(input("Enter customer Account Number To Search:"))
    for record in records:
        if(record[0]==customeraccno):
            found=True
            break
    print("-"*50)
    if(found):
        print("CUSTOMER FOUND AND VALID")
    else:
        print("CUSTOMER NOT FOUND AND INVALID")
    print("-"*50)

