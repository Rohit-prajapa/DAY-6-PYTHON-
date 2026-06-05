# def add(a, b):
#     return a+b

# print(add(2,3))


# n=int(input("enter the Number: "))

# def evenodd(n):
#     if(n%2==0):
#         print("even Number: ",n)
#     else:
#         print("odd NUmber : ",n)

# evenodd(n)


# def evenOdd(num):
#     for i in num:
#         if(i%2==0):
#             print("even number : ",i)
#         else:
#             print("odd number :",i)


# evenOdd([2,4,3,6,5,8,9])


#reverse String

# name=input("enter the String: ")

# print(name[::-1])

# name = "Rohit"

# for i in range(len(name)-1, -1, -1):
#     print(name[i], end="")

#-------------------------------------------------------------

# a=int(input("enter the first number: "))
# b=int(input("enter the second Number: "))
# def swap(a,b):
#     temp=a
#     a=b
#     b=temp
#     return a,b
# a,b=swap(a,b)
# print(a," ",b)



#--------------------------------------------------------------------
# def sum_all(*num):
#     return sum(num)

# print(sum_all(2,4,6,8,10))


#----------------------------------------------------------------------
# def details(**kwargs):
#     for key,value in kwargs.items():

#         print(key," ",value)
# details(name="rohit ", age=20, city="pune")


#------------------------------------------------------------------lambda function
# add=lambda a,b: a+b
# print(add(10,20))

# evenodd=lambda n: n%2==0 

# print(evenodd(4))

# a=lambda x,y=2: x+y
# print(a(2,5))

# rev=lambda x:x[::-1]
# print(rev("rohit"))



# n=int(input("enter the Number "))

# flag=True
# if(n<=1):
#     flag=False

# for i in range(2,n):
#     if(n%i==0):
#         flag=False
#         break


# if(flag==True):
#     print("prime Number: ")
# else:
#     print("not prime Number: ")



# num=[10,20,30,40,50]
# print(max(num))


# num=[1,5,3,7,8,5,3]

# largest=num[0]
# smxlargest=num[0]

# for i in num:
#     if i>largest:
#         largest=i

# for i in num:
#     if(i>smxlargest and i!=largest):
#         smxlargest=i

# print(largest)
# print(smxlargest)

#------------------------------------------------------------------------------------------------------

# n=int(input("enter the number "))
# temp=n
# rev=0

# while(n>0):
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10


# if(temp==rev):
#     print("it is palindrome: ")
# else:
#     print("it is not a palindrome: ")


# #------------------------------------------------------------------------------------

# balance=1000


# def withdraw(amout):
#     global balance
#     if amout<=balance:
#         balance=amout

#         print("WithDraw successfully: remaining balance :",{balance-amout})
#     else:
#         print("insufficient balance: ")
    
#     withdraw(200)


# name=input("enter the String: ")
# count=0
# for ch in name:
#     if ch in 'aeiou':
#         count+=1

# print(count)


# n=int(input("enter the number :"))

# fact=1

# for i in range(1,n+1):
#     fact=fact*i

# print(fact)


# num=[1,3,2,5,4,9,8,6]

# for i in num:
#     if(i>i+1):
#         temp=i
#         i=j
#         j=temp

#         print(num)


print(10==10.0)