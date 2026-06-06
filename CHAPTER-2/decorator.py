def my_demo(func):
    def wrapper():
        print("before hello")
        func()
        print("after hello")
    return wrapper

@my_demo
def my_hello():
    print("hello world")

my_hello()