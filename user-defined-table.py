#to show a table any given number
ch='Y'
while (ch=='y') or (ch=='Y'):
    n=int(input("enter a number:"))
    for i in range (1,11):
        p=n*i
        print(n,'×',i,'=',p)
    ch=input("Do you want to see another table y/n:")
print("goodbye")
print("hope i helped")
