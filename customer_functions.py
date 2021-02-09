import csv
from tempfile import NamedTemporaryFile
import shutil
import random 
  
def customer_id_generator():
    lst=[]
    for i in range(1,1000):
        lst.append(i)
        i=i+1
    return random.choice(lst) 

def new_customer():
    with open('customer.csv','a+') as csvfile:
        names=['customer_name','customer_id','customer_phone','customer_address']
        writer=csv.DictWriter(csvfile,fieldnames=names)
        writer.writeheader()
        print("-------------------------------------------------------------")
        customer_name=input('Enter the name of the customer : ')
        customer_id=customer_id_generator()
        print('Unique customer ID generated : ',customer_id)
        customer_phone=int(input('Enter the phone number of the customer : '))
        customer_address=input('Enter the address : ')
        print("-------------------------------------------------------------")
        print("New customer info successfully stored in our data")
        print("-------------------------------------------------------------") 
        writer.writerow({'customer_name':customer_name,'customer_id':customer_id,'customer_phone':customer_phone,"customer_address":customer_address})


def search_customer():    
    with open('customer.csv','r') as csvfile:
        print("-------------------------------------------------------------")
        name=input('Enter the name of customer:\n')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['customer_name']==name:
                print("------------------------------------------")
                print(" Name : ",row['customer_name'],'\n',"ID : ",row['customer_id'],'\n',"Phone : ",row['customer_phone'],'\n',"Address : ",row['customer_address'])
                print("------------------------------------------")
                print("Result you wanted to search")
                print("-------------------------------------------------------------")
                break

def update_customer_info():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    names=['customer_name','customer_id','customer_phone','customer_address']
    with open('customer.csv', 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=names)
        writer.writeheader()
        print("-------------------------------------------------------------")
        idno =input('Enter the id of the customer you want to modify!\n')
        print("-------------------------------------------------------------")
        for row in reader:
            if row['customer_id'] == idno:
                print('---------------------------------------------')
                print("|Enter 1 to change name                     |")
                print('---------------------------------------------')
                print('|Enter 2 to change phone number             |')
                print('---------------------------------------------')
                print('|Enter 3 to change address                  |')
                print('---------------------------------------------')
                print('|Enter 4 to go back to Customer Menu        |')
                print('---------------------------------------------')
                choice=int(input("Enter Your Choice!\n"))

                if(choice==1):
                    row['customer_name']=input("Enter the new name : ")
                    print("-------------------------------------------------------------")
                    print("New customer info updated successfully")
                    print("-------------------------------------------------------------")
                elif(choice==2):
                    row['customer_phone']=int(input("Enter the new phone number : "))
                    print("-------------------------------------------------------------")
                    print("New customer info updated successfully")
                    print("-------------------------------------------------------------")
                elif(choice==3):
                    row['customer_address']=input("Enter the new address : ")
                    print("-------------------------------------------------------------")
                    print("New customer info updated successfully")
                    print("-------------------------------------------------------------")
                elif(choice==4):
                    break
                else:
                    print("-------------------------------------------------------------")
                    print("Invalid input! Try again")
                    print("-------------------------------------------------------------") 
            row = {'customer_name':row['customer_name'],'customer_id':row['customer_id'],'customer_phone':row['customer_phone'],"customer_address":row['customer_address']}
            writer.writerow(row)

    shutil.move(tempfile.name, 'customer.csv')