def fib(n1):
   if n1<=1:
    return n1
   a=0
   b=1
   for i in range(2,n1+1):
      a,b=b,a+b
   return b
n1=9

print(f"The {n1}th fib number is: {fib(n1)}")