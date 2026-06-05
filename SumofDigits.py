n=int(input("enter the Number: "))

sum=0

while(n>0):
     ld=n%10
     sum=sum+ld
     n=n//10


print("The sum of The Given Number is :",sum)
