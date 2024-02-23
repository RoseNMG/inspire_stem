# This is a program to calculate hire purchase
# Date : 21/02/2024
# Name : Rose Mugwe

import math

# Find the hire purchase

cash_p = float(input("Enter the cash price"))
dep = float(input("Enter the deposit"))
months = float(input("Enter the number of months"))
inst = float(input("Enter the installments"))

h_p = dep + (months * inst)

print ("The hire purchase is :" ,h_p)