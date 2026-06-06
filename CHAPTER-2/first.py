# # #=========================================================================

# # file=open("demo.txt","w")
# # file.write("this is a new line code")
# # file.close()

# # #=========================================================================
# # file = open("demo.txt", "r")
# # data = file.read()
# # print(data)
# # #===============================================
# # f = open("demo.txt", "w")

# # f.write("Hello Rohit")

# # f.close()

# # #==============================
# # f = open("demo.txt", "r")

# # data = f.read()

# # print(data)

# # f.close()

# # #======================================================================================
# # f = open("demo.txt", "r")

# # print(f.readline())

# # f.close()

# # #==============================================
# # f = open("demo.txt", "r")

# # print(f.readlines())

# # f.close()

# # #==============================================================
# # f = open("demo.txt", "a")

# # f.write("\nPython")

# # f.close()

# # #==================================================
# # f = open("newfile.txt", "x")

# # f.close()



# #+=================================================================

# # file=open("newfile.txt","w")
# # file.write("i am learning pyhton")
# # file.close()

# # file=open("newfile.txt","r")
# # data=file.read()
# # print(data)
# # file.close()


# # f=open("newfile.txt","w")
# # f.write("hello rohit")
# # f.close()

# # file=open("newfile","r")
# # d=file.read()
# # print(d)
# # file.close()


# #===============================================================
# # file=open("mydemo.txt","w")
# # file.write("hello rohit")
# # file.close()

# # f=open("mydemo.txt","r")
# # data=f.read()

# # print(data)
# # f.close()


# file = open("mydemo.txt", "r")

# data = file.read()

# print("Lines =", len(data.splitlines()))
# print("Words =", len(data.split()))
# print("Characters =", len(data))

# vowels = 0

# for ch in data.lower():
#     if ch in "aeiou":
#         vowels += 1

# print("Vowels =", vowels)

# file.close()



# with open("mydemo.txt","r") as f:
#     for line in f:
#         print(line)
        



# import os

# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
#     print("file is deleted: ")









#========================================================================================================




###this is not example of threding
# def nik():
#     for i in range(3):
#         print("rohit")


# def dev():
#     for i in range(3):
#         print("prajapati")

# nik()
# dev()



#Thread

# from time import sleep
# from threading import Thread

# class A(Thread):
#     def run(self):
#         for i in range(3):
#             print("rohit ")
#             sleep(3)

# class B(Thread):
#     def run(self):
#         for i in range(3):
#             print("prajapati")
#             sleep(3)

# t1=A()
# t2=B()

# t1.start()
# t2.start()



#=============================================]

# class Animal:
#     def speak(self):
#         print("animal")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# d = Dog()
# c = Cat()

# d.speak()
# c.speak()


# class father():
#     def king(self):
#         print("i am king of my family: ")

# class son(father):
#     def prince(self):
#         print("i am prince: ")

# f=father()
# t=son()

# f.king()
# t.prince()




class GrandFather:
    def abc(self):
        print("i am god father")

class father:
    def xyz(self):
        print("i am father")


class son(GrandFather,father):
    def que(self):
        print(" i am son: ")


t1=son()
t1.abc()
t1.xyz()
t1.que()



