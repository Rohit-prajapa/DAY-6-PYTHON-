
# def square(n):
#     for i in range(1,n+1):
#         yield i*i

# g=square(5)
# print(next(g))
# print(next(g))
# print(next(g))

#----------------------------------------------------------------------------
def even_odd(n):
    for i in range(1,n+1):
        if(i%2==0):
            yield "even"
        else:
            yield "odd"

g=even_odd(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#=======================================================================================================
