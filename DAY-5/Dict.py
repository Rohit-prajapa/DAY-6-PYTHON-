#Feature Of Dict
# ✅ Mutable (can be changed)

# ✅ Stores data in key-value pairs

# ✅ Keys must be unique

# ✅ Values can be duplicate

# ✅ Ordered (Python 3.7+)

d={
    "name ":"rohit",
    "roll_no":40
}

print(d)

d={}
print(type(d))


My_dict={
    "name ":"rohit",
    "age ":20
}

#update age
My_dict["age"]=30
print(My_dict)

#adding new

My_dict["city"]="varanasi"

print(My_dict)

#delecting

My_dict.pop("age")
print(My_dict)

#Accessing Elements

student={
    "name ":"rohit ",
    "age ":20
}

print(student["age "])

print(student.get("age"))

#Adding Elements

student = {
    "name": "Rohit"
}
student["age"] = 20
print(student)


#Updating Values
student["age"] = 21
print(student)

#Removing Elements
student.pop("age")

#del
del student["name"]

#clear()
student.clear()


#Dictionary Methods:
d = {
    "name":"Rohit",
    "age":20
}

print(d.keys())


#square Fumction

square={
   "a":2,
   "b":3,
   "c":4
}

for i in square:
    square[i]**=2

print(square)


prectics={
    "a ":2,
    "b ":3,
    "c ":4,    
    "d ":5,
    "e ":6
}

for key,value in prectics.items():
    if(value<4):
        print(key,value)
