def my_demo(fun):
    def wrapper(b):
        print("before Upper case: ")
        result=fun(b)
        print(result.upper())
        print("after upperCase") 
    
    return wrapper
@my_demo
def fun(a):
    return a
fun("rohit")

#-----------------------------------------------------------------------------------------------------
def my_demo(fun):
    def wrapper(a,b):
        print("before power: ")
        result=fun(a,b)
        print(result)
        print("after power: ")
    return wrapper

@my_demo
def power(a,b):
    return a**b

power(2,3)

#--------------------------------------------------------------------------------------------------
