def adder(f1, f2):
   def h(n):
       return f1(f2(n)) + n
   return h

def square(n):
   return n ** 2
def identity(n):
   return n

a1 = adder(identity, square)
print(a1(4))

a2 = adder(a1, identity)
print(a2(4))

print(a2(5))

a3 = adder(a1, a2)
print(a3(4))

