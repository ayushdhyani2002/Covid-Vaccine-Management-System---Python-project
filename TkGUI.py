from tkinter import *
import sys
import vaccine_functions
import supplier_functions
import customer_functions
import report_functions
import invoicing_functions
import menu_function



#vaccine Menu
def vaccine_menu():
    vaccine_menu_window = Tk()
    vaccine_menu_window.geometry('350x200')
    vaccine_menu_window.title("Covid Vaccine Management Software")
    lbl = Label(vaccine_menu_window, text="Vaccine Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(vaccine_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(vaccine_menu_window, text="Add New vaccine",fg="red", command=vaccine_functions.add_vaccine)
    btn1.grid(column=0, row=2)
    btn2 = Button(vaccine_menu_window, text="Search vaccine",fg="red", command=vaccine_functions.search_vaccine)
    btn2.grid(column=0, row=3)
    btn3 = Button(vaccine_menu_window, text="Update vaccine info",fg="red", command=vaccine_functions.update_vaccine)
    btn3.grid(column=0, row=4)
    btn4 = Button(vaccine_menu_window, text="vaccines to be purchased",fg="red", command=vaccine_functions.vaccine_to_be_purchased)
    btn4.grid(column=0, row=5)
    vaccine_menu_window.mainloop()

#Customer Menu
def customer_menu():
    c_menu_window = Tk()
    c_menu_window.geometry('350x200')
    c_menu_window.title("Covid Vaccine Management Software")
    lbl = Label(c_menu_window, text="Customer Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(c_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(c_menu_window, text="Search Customer",fg="red", command=customer_functions.search_customer)
    btn1.grid(column=0, row=2)
    btn2 = Button(c_menu_window, text="New Customer",fg="red", command=customer_functions.new_customer)
    btn2.grid(column=0, row=3)
    btn3 = Button(c_menu_window, text="Update Customer Info",fg="red", command=customer_functions.update_customer_info)
    btn3.grid(column=0, row=4)
    c_menu_window.mainloop()

#Supplier Menu
def supplier_menu():
    s_menu_window = Tk()
    s_menu_window.geometry('350x200')
    s_menu_window.title("Covid Vaccine Management Software")
    lbl = Label(s_menu_window, text="Supplier Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(s_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(s_menu_window, text="Search Supplier",fg="red", command=supplier_functions.search_supplier)
    btn1.grid(column=0, row=2)
    btn2 = Button(s_menu_window, text="New Supplier",fg="red", command=supplier_functions.create_supplier)
    btn2.grid(column=0, row=3)
    btn3 = Button(s_menu_window, text="Update Supplier Info",fg="red", command=supplier_functions.update_supplier_info)
    btn3.grid(column=0, row=4)
    s_menu_window.mainloop()

#Report Menu
def report_menu():
    r_menu_window = Tk()
    r_menu_window.geometry('350x200')
    r_menu_window.title("Covid Vaccine Management Software")
    lbl = Label(r_menu_window, text="Supplier Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(r_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(r_menu_window, text="Day Sales",fg="red", command=report_functions.day_sale)
    btn1.grid(column=0, row=2)
    btn2 = Button(r_menu_window, text="Month Sales",fg="red", command=report_functions.month_sale)
    btn2.grid(column=0, row=3)
    btn3 = Button(r_menu_window, text="Day Purchase",fg="red", command=report_functions.day_purchase)
    btn3.grid(column=0, row=4)
    btn3 = Button(r_menu_window, text="Month Purchase",fg="red", command=report_functions.month_purchase)
    btn3.grid(column=0, row=5)
    btn3 = Button(r_menu_window, text="Profit Report",fg="red", command=report_functions.profit_report)
    btn3.grid(column=0, row=6)
    r_menu_window.mainloop()

#Invoicing Menu
def invoicing_menu():
    r_menu_window = Tk()
    r_menu_window.geometry('350x200')
    r_menu_window.title("Covid Vaccine Management Software")
    lbl = Label(r_menu_window, text="Invoice Menu!")
    lbl.grid(column=0, row=0)
    lbl2 = Label(r_menu_window, text="What would you like to do!")
    lbl2.grid(column=0, row=1)
    btn1 = Button(r_menu_window, text="Supplier Invoice",fg="red", command=invoicing_functions.sup_invoice)
    btn1.grid(column=0, row=2)
    r_menu_window.mainloop()

#Main Menu
window = Tk()
window.geometry('350x200')
window.title("Covid Vaccine Management Software")
lbl = Label(window, text="Welcome to Covid Vaccine Management Software!")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="What would you like to do!")
lbl2.grid(column=0, row=1)
btn1 = Button(window, text="vaccine Menu",fg="red", command=vaccine_menu)
btn1.grid(column=0, row=2)
btn2 = Button(window, text="Customer Menu",fg="red", command=customer_menu)
btn2.grid(column=0, row=3)
btn3 = Button(window, text="Supplier Menu",fg="red", command=supplier_menu)
btn3.grid(column=0, row=4)
btn4 = Button(window, text="Report Menu",fg="red", command=report_menu)
btn4.grid(column=0, row=5)
btn5 = Button(window, text="Invoicing Menu",fg="red", command=invoicing_menu)
btn5.grid(column=0, row=6)

window.mainloop()

