def even_odd(n):
    for i in range(n+1):
        if(i%2==0):
            yield i


g=even_odd(10)
print(next(g))
print(next(g))