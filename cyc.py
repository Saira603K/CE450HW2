def cyc(g1, g2, g3):
    def g(n):
        def final(x):
            if n == 0:
                return x
            else:
                return cyc(g2, g3, g1)(n-1)(g1(x))
        return final
    return g


def add_one(x):
    return x + 1


def times_two(x):
    return x * 2


def add_three(x):
    return x + 3


my_cyc = cyc(add_one, times_two, add_three)
h = my_cyc(0)
print(h(5))

h = my_cyc(2)
print(h(1))

h = my_cyc(3)
print(h(2))

h = my_cyc(4)
print(h(2))

h = my_cyc(6)
print(h(1))
