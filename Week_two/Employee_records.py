# This is program to show employee records
# Date : 21/02/2024
# Name : Rose Mugwe

print("---EMPLOYEE REGISTER---")
print("  1. Rose Nyambura ")
print("  2. Tracy Kanyora ")
print("  3. Angie Muthoni ")
print(" --- ")

name = input("Enter employee name :")

print("Name :" ,name)
if name == "Rose Nyambura":
    age = 24
    sal = 55000
    bon = 7000
    tot = sal + bon
    print("Age : ",age)
    print("Salary : ",sal)
    print("Bonus : ",bon)
    print("Total : ",tot)

    print("----------")

    print("Due to new revision :")
    new_s = sal + (0.3 * sal)
    new_b = bon - 5000
    new_tot = new_s + new_b

    print("New salary : ",new_s)
    print("New bonus : ",new_b)
    print("New total : ",new_tot)
elif name == "Tracy Kanyora":
     age = 29
     sal = 40000
     bon = 6300
     tot = sal + bon
     print("Age : ",age)
     print("Salary : ",sal)
     print("Bonus : ",bon)
     print("Total : ",tot)

     print("----------")               

     print("Due to new revision :")
     new_s = sal + (0.3 * sal)
     new_b = bon - 5000
     new_tot = new_s + new_b

     print("New salary : ",new_s)
     print("New bonus : ",new_b)
     print("New total : ",new_tot)
elif name == "Angie Muthoni":
     age = 32
     sal = 58000
     bon = 6700
     tot = sal + bon
     print("Age : ",age)
     print("Salary : ",sal)
     print("Bonus : ",bon)
     print("Total : ",tot)

     print("----------")               

     print("Due to new revision :")
     new_s = sal + (0.3 * sal)
     new_b = bon - 5000
     new_tot = new_s + new_b

     print("New salary : ",new_s)
     print("New bonus : ",new_b)
     print("New total : ",new_tot)
 
     
    

