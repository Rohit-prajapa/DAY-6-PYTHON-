n=int(input("enter the Number: "))

rev=0

while(n>0):
    ld=n%10
    rev=rev*10+ld
    n=n//10



print("the Reverse of The Given Number is :",rev)