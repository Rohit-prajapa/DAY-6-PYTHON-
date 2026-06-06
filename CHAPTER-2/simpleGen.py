def fun():
    yield 10
    yield 20
    yield 30

g=fun()
print(next(g))
print(next(g))
print(next(g))