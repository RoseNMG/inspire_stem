# This is a program to show multiplication tables
# Date : 22/02/2024
# Name : Rose Mugwe

num = int(input("Display multiplication table of "))
for i in range (1 , 11):
    print(num, 'x', i,'=', num*i)

print("\n\n")   

def main():
    n = 10

    for i in range(1 ,n+1):
        for j in range(1, n+1):
            print(f"{i *j:4}", end= "")
        print()    
    pass
if __name__ == "__main__":
    main()
