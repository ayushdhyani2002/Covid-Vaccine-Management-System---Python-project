import csv
import random
import sys
from tempfile import NamedTemporaryFile
import shutil
import datetime
d = datetime.datetime.now()

def vaccine_id_generator():
    lst=[]
    for i in range(1,1000):
        lst.append(i)
        i=i+1
    return random.choice(lst)


def add_vaccine():
	with open('vaccine.csv','a+') as csvfile:
		columns = ['vaccine_name','vaccine_id','sale','unit','quantity','min_quantity', 'comp_name', 'sup_id','to_purchase']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		print("-----------------------------------------------------")
		vaccine_name = input("Enter vaccine name : ")
		with open('vaccine.csv','r+') as csfile:
			reader=csv.DictReader(csfile)
			for row in reader:
				if row['vaccine_name'] == vaccine_name:
					print("Vaccine Already exists.")
					return

		vaccine_id = vaccine_id_generator()
		print('Unique vaccine ID generated : ',vaccine_id)
		sale = float(input("Enter sale price : "))
		unit = float(input("Enter cost price : "))
		quantity = int(input("Enter quantity : "))
		min_quantity = int(input("Enter min quantity to maintain : "))
		comp_name = input("Enter company name : ")
		sup_id = int(input("Enter supplier ID : "))
		print("-----------------------------------------------------")
		print("All the info of new vaccine is added in our data")
		print("-----------------------------------------------------")
		cost = unit * quantity
		to_purchase = min_quantity - quantity
		if quantity >min_quantity:
			to_purchase = 0
		writer.writerow({'vaccine_name':vaccine_name,'vaccine_id':vaccine_id,'sale':sale,'unit':unit,'quantity':quantity,\
		'min_quantity':min_quantity,'comp_name':comp_name,'sup_id':sup_id,'to_purchase':to_purchase})

		
		with open('purchase.csv','a+') as csvfile:
			purchase_date= d.strftime("%d")
			purchase_month= d.strftime("%m")
			purchase_year = d.strftime("%Y")
			columns = ['vaccine_name','vaccine_id','unit','quantity','purchase_date', 'purchase_month','purchase_year','sup_id','cost']
			writer = csv.DictWriter(csvfile,fieldnames = columns)
			
			writer.writerow({'vaccine_name':vaccine_name,'vaccine_id':vaccine_id,'unit':unit,'quantity':quantity,'purchase_date':purchase_date,'purchase_month':purchase_month,'purchase_year':purchase_year,'sup_id':sup_id,'cost':cost})


def search_vaccine():
    with open('vaccine.csv','r') as csvfile:
        print("-----------------------------------------------------")
        name=input('Enter the vaccine to search : ')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['vaccine_name'] == name:
                print(' Name :', row['vaccine_name'],'\n','Quantity : ',row['quantity'],'\n','Price : ',row['sale'])
                print("-----------------------------------------------------")
                print("Result you wanted to search")
            else:
                print("-----------------------------------------------------")
                print("There's no such vaccine in our records")
                print("Please try again!")
                print("-----------------------------------------------------")
                break
        print("-----------------------------------------------------")        


def update_vaccine():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    columns = ['vaccine_name','vaccine_id','sale','unit','quantity','min_quantity','comp_name', 'sup_id','to_purchase']
    with open('vaccine.csv', 'r+') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()
        print("-----------------------------------------------------")
        vaccine_name =input('Enter the name of the vaccine you want to modify : ')
        for row in reader:
            if row['vaccine_name'] == vaccine_name:
            	print('---------------------------------------------')
            	print('|Enter 1 To update vaccine Name             |')
            	print('---------------------------------------------')
            	print('|Enter 2 To update Cost price               |')
            	print('---------------------------------------------')
            	print('|Enter 3 To update Sale price               |')
            	print('---------------------------------------------')
            	print('|Enter 4 To update supplier ID              |')
            	print('---------------------------------------------')
            	choice=int(input())
            	if(choice==1):
            		row['vaccine_name']=input("Enter the new name : ")
            		print("-----------------------------------------------------")
            		print("New data updated successfully")
            		print("-----------------------------------------------------")
            	elif(choice==2):
            		row['cost']=input("Enter the new cost price : ")
            		print("-----------------------------------------------------")
            		print("New data updated successfully")
            		print("-----------------------------------------------------")
            	elif(choice==3):
            		row['sale']=input("Enter the new sale price : ")
            		print("-----------------------------------------------------")
            		print("New data updated successfully")
            		print("-----------------------------------------------------")
            	elif(choice==4):
            		row['sup_id']=input("Enter the new supplier ID : ")
            		print("-----------------------------------------------------")
            		print("New data updated successfully")
            		print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("There's no such vaccine in our records")
                print("Please try again!")
                print("-----------------------------------------------------")
                break
            row ={'vaccine_name':row['vaccine_name'],'vaccine_id':row['vaccine_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],'min_quantity':row['min_quantity'],'comp_name':row['comp_name'],'sup_id':row['sup_id'],'to_purchase':row['to_purchase']}
            writer.writerow(row)
    shutil.move(tempfile.name, 'vaccine.csv')

    
def vaccine_to_be_purchased():
	count = 0
	with open('vaccine.csv','r') as csvfile:
		reader=csv.DictReader(csvfile)
		print("-----------------------------------------------------")
		print("These are list of vaccines of to be purchased")
		print("-----------------------------------------------------")
		for row in reader:
			if int(row['to_purchase']) >0:
				count+=1
				print("-----------------------------------------------------")
				print(' Name : ', row['vaccine_name'],'\n','Quantity : ',row['quantity'],'\n','Minimum Quantity : ',row['min_quantity']\
				,'\n','To be purchased : ',row['to_purchase'],'\n','Supplier ID : ',row['sup_id'])
				print("-----------------------------------------------------")
	if count == 0:
		print("-----------------------------------------------------")
		print("No vaccine to be purchased.\n")
		print("-----------------------------------------------------")