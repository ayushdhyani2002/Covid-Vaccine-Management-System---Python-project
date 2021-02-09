import csv
from tempfile import NamedTemporaryFile
import shutil
import random

def supplier_id_generator():
    lst=[]
    for i in range(1,1000):
        lst.append(i)
        i=i+1
    return random.choice(lst) 

def create_supplier():
    with open('supplier.csv', 'a+') as csvfile:
        columns = ['sup_name', 'sup_id', 'sup_city', 'sup_contact', 'sup_email']
        writer = csv.DictWriter(csvfile, fieldnames = columns)
        print("------------------------------------------------------------------")
        sup_name = input("Enter New Supplier's Name : ")
        sup_id = supplier_id_generator()
        print('Unique Supplier ID Generated : ', sup_id)
        sup_city = input("Enter New Supplier's City : ")
        sup_contact = int(input("Enter New Supplier's Contact Number : "))
        sup_email = input("Enter New Supplier's Email Id : ")
        writer.writerow({'sup_name':sup_name, 'sup_id':sup_id, 'sup_city':sup_city, 'sup_contact':sup_contact, 'sup_email':sup_email})
        print("==================================================================")
        print("Your data is successfully saved on our records !")
        print("==================================================================")

def search_supplier():
    with open('supplier.csv','r') as csvfile:
        print("------------------------------------------------------------------")
        name=input('Enter Supplier Name!\n')
        reader=csv.DictReader(csvfile)
        for r in reader:
            if r['sup_name'] == name:
                print("------------------------------------------------------------------")
                print("Your required data -")
                print("------------------------------------------------------------------")
                print('Name : ', r['sup_name'], '\n', 'Id : ', r['sup_id'],'\n', 'City : ', r['sup_city'], '\n', 'Contact No :', r['sup_contact'], '\n', 'Email id : ', r['sup_email'])
                print("------------------------------------------------------------------")
                break

def update_supplier_info():
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        columns = ['sup_name', 'sup_id', 'sup_city', 'sup_contact', 'sup_email']
        with open('supplier.csv', 'r') as csvfile, tempfile:
                reader = csv.DictReader(csvfile)
                writer = csv.DictWriter(tempfile, fieldnames=columns)
                writer.writeheader()
                print("------------------------------------------------------------------")
                suppp_name=input('Enter the name of the supplier you want to modify!\n')
                for r in reader:
                        if r['sup_name'] == suppp_name:
                                print('---------------------------------------------')
                                print('|Enter 1 to update supplier name.           |')
                                print('---------------------------------------------')
                                print('|Enter 2 to update supplier id.             |')
                                print('---------------------------------------------')
                                print('|Enter 3 to update supplier city.           |')
                                print('---------------------------------------------')
                                print('|Enter 4 to update supplier contact no.     |')
                                print('---------------------------------------------')
                                print('|Enter 5 to update supplier email id.       |')
                                print('---------------------------------------------')
                                choice=int(input('Enter your choice!\n'))
                                if(choice==1):
                                    r['sup_name']=input("Enter updated name : ")
                                    print("==================================================================")
                                    print("Supplier info updated successfully!")
                                    print("==================================================================")
                                elif(choice==2):
                                    r['sup_id']=int(input("Enter updated id : "))
                                    print("==================================================================")
                                    print("Supplier info updated successfully!")
                                    print("==================================================================")
                                elif(choice==3):
                                    r['sup_city']=input("Enter updated city : ")
                                    print("==================================================================")
                                    print("Supplier info updated successfully!")
                                    print("==================================================================")
                                elif(choice==4):
                                    r['sup_contact']=int(input("Enter updated contact : "))
                                    print("==================================================================")
                                    print("Supplier info updated successfully!")
                                    print("==================================================================")
                                elif(choice==5):
                                    r['sup_email']=input("Enter updated email id : ")
                                    print("==================================================================")
                                    print("Supplier info updated successfully!")
                                    print("==================================================================")
                                else:
                                    print("------------------------------------------------------------------")
                                    print("Invalid Input!\n")
                                    print("------------------------------------------------------------------")
                        r = {'sup_name':r['sup_name'], 'sup_id':r['sup_id'], 'sup_city':r['sup_city'], 'sup_contact':r['sup_contact'], 'sup_email':r['sup_email']}
                        writer.writerow(r)
        shutil.move(tempfile.name, 'supplier.csv')