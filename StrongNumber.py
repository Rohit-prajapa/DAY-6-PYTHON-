n=int(input("enter the Number: "))

temp=n

sum=0

while(n>0):
    ld=n%10

    fact=1
    for i in range(1,ld+1):
        fact=fact*i
    
    sum=sum+fact
    n=n//10


if(sum==temp):
    print("it is a Strong Number: ")
else:
    print("it is not a Strong Number: ")
