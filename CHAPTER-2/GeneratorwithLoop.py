def count(n):
    for i in range(n+1):
        if(n%4==0):
         yield i

g=count(10)
print(next(g))
print(next(g))
print(next(g))