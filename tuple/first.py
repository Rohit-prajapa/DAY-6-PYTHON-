#Stores multiple values in a single variable.
# Is ordered (elements have fixed positions).
# Is immutable (cannot be changed after creation).
# Allows duplicate values.
#indexing & slicing

t=(10,20,30,40)
b=list(t)
print(type(b))
print(b)

list_tuple=(1,2,(3,4,5))
print(list_tuple)


a=(10,20,30,40)
print(a.index(40))

b=(1,2,2,2,3,4,5)
print(b[0:5])

print(b[:3])
print(b[2:])

print(b[:])
print(b[0:6:2])

print(b[::3])


t=(10,20,30,40,50)

rev=t[::-1]
print(rev)
