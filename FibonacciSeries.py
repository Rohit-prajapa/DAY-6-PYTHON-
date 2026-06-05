n=int(input("enter the Number: "))

first=0
second=1
NextElement=0

print(first," ",second)

for i in range(2,n+1):
    NextElement=first+second
    first=second
    second=NextElement


print(NextElement)
