def fib(n=10): 
 f = [0,1]
 if n<=2:
  return f[:n]
 for i in range(2, n):
  print i  
  f[len(f):]=[f[i-2]+f[i-1]]
 return f

 

    
    

