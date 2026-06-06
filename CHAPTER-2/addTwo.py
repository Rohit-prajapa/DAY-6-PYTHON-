def my_add(add):
    def wrapper(a,b):
        print("before add:")
        result = add(a,b)
        print(result)
        print("after add")
    return wrapper

@my_add
def add(a,b):
    return a+b

add(2,3)