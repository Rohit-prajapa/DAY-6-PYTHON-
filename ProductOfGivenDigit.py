n=int(input("enter the Number: "))

product=1

while(n>0):
    ld=n%10
    product=product*ld
    n=n//10

print("the Product of the Given Number is :",product)