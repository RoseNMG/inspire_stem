# Strings in python
# Date : 22/02/2024
# Name : Rose Mugwe

city = "nairobi"

print(city[0]) # n
print(city[1]) # a
print(city[2]) # i
print(city[3]) # r
print(city[4]) # o
print(city[-1]) # b
print(city[-2]) # i


# convert to uppercase


print(city)
print("\n\n") # creates a new line
print(city.upper())

name = "ROSE"
print(name)
print(name.lower()) # converts string to lowercase

town = "          Naivasha          "

print(town)
print("\t") # new tab
print(town.strip())

# add two strings

f_name = "Rose"
s_name = "Nyambura"

full_name = f_name + s_name

print(full_name)

# replacing a character

fruit = "OrangeOOO"

print(fruit.replace("O" , "Y"))

subject = "Physical:Sciences"

print(subject.split(":"))

Age = 17
Height = 1.2

print("I am {0} years old and {1} meters tall" .format(Age,Height))

# Reverse string

month = "february"
result = ''.join(reversed(month))
print(result)

