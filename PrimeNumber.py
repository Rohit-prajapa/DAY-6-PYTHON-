n=int(input("enter the Number : "))

flag=True

if(n==1):
    flag=False

for i in range(2,n):
    if(n%i==0):
        flag=False
        break


if(flag==True):
    print("Prime Number : ")
else:
    print("not Prime Number: ")