#List is mutable, List can strore diff -2 data type, list is order and list is allowed duplicate element
num=[1,2,3,4,5]
num.append(6)
print(num)

#diff b/w append and insert

num.insert(1,8)
print(num)

#extands

num.extend([10,20])
print(num)

#pop opretion 

num.pop()
print(num)

num.pop()
print(num)

a=[1,2,3,4]
b=[5,6,7]

a.extend(b)

print(a)

b=[1,2,3,2,4,5]
b.count(2)
print(b)