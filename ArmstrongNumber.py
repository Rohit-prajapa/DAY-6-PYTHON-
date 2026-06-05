n=int(input("enter the Number "))

temp=n

sum=0

while(n>0):
    ld=n%10
    sum=sum+ld*ld*ld
    n=n//10


if(sum==temp):
    print("it is a ArmStrong Number ")
else:
    print("it is Not a ArmStrong Number: ")