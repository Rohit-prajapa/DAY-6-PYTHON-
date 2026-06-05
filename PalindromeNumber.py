n=int(input("enter the NUmber: "))

temp=n
rev=0
while(n>0):
    ld=n%10
    rev=rev*10+ld
    n=n//10


if(rev==temp):
    print("it is palindrome Number: ")
else:
    print("it is not a palindrome: ")