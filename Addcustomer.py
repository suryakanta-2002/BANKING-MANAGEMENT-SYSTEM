#EmployeeAdd.py<---Module Name
import pickle
import random
class InValidNameError(Exception):pass
class SpaceError(BaseException):pass
class ZeroNameLengthError(Exception):pass
#NameValidation.py<--Module Name
def validatename(customername):
    if(len(customername)==0):
        raise ZeroNameLengthError
    elif(customername.isspace()):
        raise SpaceError
    else:
        res=True
        words=customername.split()
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            return customername
        else:
            raise InValidNameError

def isunique(lst): # lst=[600,"KV",0.0,"NIT"]
    with open("customerdata.txt","rb") as fp:
        records=[]
        while(True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        found=True
        for record in records:
            if (record[0]==lst[0]):
                found=False
                break
        return found
def addcustomer():
    with open("customerdata.txt", "ab") as fp:
        while (True):
            try:
                print("-" * 50)
                #customeraccno= int(input("\tEnter New Customer Account Number:"))
                customeraccno=random.randint(10000000,99999999)
                customername= input("\tEnter Customer Name:")
                customername=validatename(customername)
                customerbal=0.0
                while(True):
                    customerpin = input("\tEnter 4-digit PIN: ")
                    confirm_pin = input("\tConfirm Your PIN: ")

                    if customerpin == confirm_pin and customerpin.isdigit() and len(customerpin) == 4:
                        print("PIN set successfully!")
                        break
                    else:
                        print("Invalid Or Mismatched PIN! try-again")
                print("-" * 50)
                lst =list()  # Create empty list for adding customers data
                # append customer data to lst object
                lst.append(customeraccno)
                lst.append(customername)
                lst.append(customerbal)
                lst.append(customerpin)
                # Save the Iterable object content to the file
                if(isunique(lst)):
                    pickle.dump(lst, fp)
                    print("\tCustomer Account Created Successfully")
                else:
                    print("\tcustomer Account Number Already exist-try with Unique Account Number")
                print("-" * 50)
                ch = input("\tDo You Want To Enter Another Customer Details(yes/no):")
                if ch.lower() == "no":
                    break
                print("-"* 50)
            except ValueError:
                print("\tDon't Enter alnums,strs and symbols for Customer Account Number")
            except SpaceError:
                print("\tDON'T ENTER SPACE FOR Your NAME-Try Again")
            except ZeroNameLengthError:
                print("\tENTER FOR YOUR NAME-Try Again")
            except InValidNameError:
                print("\tInvalid Customer Name-Try-again")