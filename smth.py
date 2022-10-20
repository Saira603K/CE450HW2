def smth(g, dx):
    return lambda x: (g(x - dx) + g(x) + g(x + dx)) / 3

def square(n):
    return n**2


print(round(smth(square,1)(0),3))