def intsct(f1, x):
   def g(f2):
       if f2(x) == f1(x):
           return True
       else:
           return False
   return g

def square(n):
   return n ** 2
def identity(n):
   return n
def triple(n):
   return n + n + n
def increment(n):
   return n +1

a1 = intsct(square, 3)
print(a1(triple))
print(a1(increment))
a2 = intsct(identity, 1)
print(a2(square))
print(a2(triple))