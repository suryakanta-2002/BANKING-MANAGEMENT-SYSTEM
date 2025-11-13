#Deletcustomer.py <----Module Name
import pickle
def deletecustomer():
    with open("customerdata.txt","rb") as fp:
        records = []
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        # display records
    found = False
    customeraccno= int(input("Enter The Customer Account Number for delete the record:"))
    for index in range(len(records)):
        if (records[index][0] == customeraccno):
            found = True
            recindex = index
            break
    if (found):
        records.pop(recindex)
        # Place the records from main memory into the file of secondary memory
        with open("customerdata.txt", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("Customer Account Closed Successfilly--verify")
    else:
        print("Customer Account does not Exist")