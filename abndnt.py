def abndnt(n):
   sum = 0
   for i in range(1, n + 1):
       if n % i == 0:
           #print(i)
           sum = sum + i
   sum2 = sum - n
   #print(sum2)
   if sum2 < n or sum2 == n:
       return print(False)
   else:
       print(True)

num1 = 12
abndnt(num1)
num2 = 14
abndnt(num2)
num3 = 16
abndnt(num3)
num4 = 20
abndnt(num4)
num5 = 22
abndnt(num5)