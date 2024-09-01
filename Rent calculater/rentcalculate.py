
#input

rent = int(input("Enter your hostle/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spen = "))
charge_per_unit =  int(input("Enter the charge per unit = "))
person = int(input("Enter the  number of person living in room/flat =  "))


#output
total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill) //person

print("Each person will pay = " , output)
