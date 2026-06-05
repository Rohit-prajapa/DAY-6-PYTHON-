# a=set()
# print(type(a))

# s={10,20,30,40}

# print(s)

# a={1,2,3,4}
# b={5,6,7}

# print(a.union(b))

# print(a.intersection(b))

#adding element 

a={10,20,30}
a.add(40)
print(a)

#print set
s = {10, 20, 30, 20, 10}

print(s)

#Empty set
s = set()
print(type(s))


#it is not Empty Set
s={}
print(type(s))

#travelling in set
b={10,20,30,40}

for i in b:
    print(i)


#remove Element
a.remove(20)
print(a)


#update Element
s1 = {10,20}

s1.update([30,40,50])

print(s1)

#Duplicate Values Not Allowed

s = {10, 20, 30, 20, 10}

print(s)

#discard()

s = {10,20,30}

s.discard(100)

print(s)


#pop()

s = {10,20,30}

s.pop()

print(s)

#clear()
s = {10,20,30}

s.clear()

print(s)


###Set Functions

#len()


#max()
s = {10,50,20}

print(max(s))

#min()

s = {10,50,20}

print(min(s))

#sum()

s = {10,20,30}

print(sum(s))

#Membership Operators

#in
s = {10,20,30}

print(20 in s)

#not in
print(50 not in s)


##Set Operations

#Union
A = {1,2,3,4}
B = {3,4,5,6}

print(A.union(B))
print(A.intersection(B))

#Difference
print(A-B)


#Symmetric Difference
#Elements not common in both sets.
print(A^B)

#Subset
A = {1,2}
B = {1,2,3,4}

print(A.issubset(B))


#Superset
A = {1,2}
B = {1,2,3,4}

print(B.issuperset(A))

#Type Casting

lst = [1,2,2,3,4]

s = set(lst)

print(s)


#Tuple → Set
