def fib(n=10): 
 fibs = [0,1]
 if n<=2:
  return fibs[:n]
 for i in range(2, n):
  print i  
  fibs[len(fibs):]=[fibs[i-2]+fibs[i-1]]
 return fibs
