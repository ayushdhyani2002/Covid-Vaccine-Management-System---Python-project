import csv
import random
from tempfile import NamedTemporaryFile
import shutil
import datetime
d = datetime.datetime.now()
date= d.strftime("%d")
month= d.strftime("%m")
year = d.strftime("%Y")

def vaccine_id_generate():
    lst=[]
    for i in range(1,1000):
        lst.append(i)
        i=i+1
    return random.choice(lst) 

def sup_invoice():
	print("---------------------------------------------------------------------")
	vaccine_name = input("Enter vaccine name : ")
	vaccine_id= vaccine_id_generate()
	print('Unique vaccine ID generated : ',vaccine_id)
	quantity = int(input("Enter quantity : "))
	sup_id = input("Enter supplier id : ")
	units=int(input("Enter current units : "))
	print("---------------------------------------------------------------------")    
	cost = quantity * units

	with open('purchase.csv','a+') as csvfile:
		columns = ['vaccine_name','vaccine_id','unit','quantity','purchase_date', 'purchase_month','purchase_year', 'sup_id','cost']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		writer.writerow({'vaccine_name':vaccine_name,'vaccine_id':vaccine_id,'unit':units,'quantity':quantity,'purchase_date':date,'purchase_month':month,'purchase_year':year,'sup_id':sup_id,'cost':cost})
	print("========================================================")
	print("Your data is successfully saved on our records!")
	print("========================================================")
	
	tempfile = NamedTemporaryFile(mode='w', delete=False)
	with open('vaccine.csv','r') as csvfile,tempfile:
		
		columns = ['vaccine_name','vaccine_id','sale','unit','quantity','min_quantity','comp_name', 'sup_id','to_purchase']	
		reader = csv.DictReader(csvfile)
		writer = csv.DictWriter(tempfile, fieldnames=columns)
		writer.writeheader()
		
		for row in reader:
			if row['vaccine_name'] == vaccine_name:
				vaccine_id = row['vaccine_id']
				unit = float(row['unit'])
				row['quantity'] = int(row['quantity']) + quantity
				if int(row['quantity'])<int(row['min_quantity']):
					row['to_purchase'] = int(row['min_quantity']) -int(row['quantity'])
				else:
					row['to_purchase'] = 0
			row = {'vaccine_name':row['vaccine_name'],'vaccine_id':row['vaccine_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
			'min_quantity':row['min_quantity'],'comp_name':row['comp_name'],'sup_id':row['sup_id'],'to_purchase':row['to_purchase']}
			writer.writerow(row)
	shutil.move(tempfile.name, 'vaccine.csv')
	print("---------------------------------------------------------------------") 