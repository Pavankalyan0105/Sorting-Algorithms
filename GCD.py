def gcd(a,b):
  if(b==0):
      return a
  return gcd(b,a%b)
  
 a = int(input())
 
 b = int(input())
 
 gcd(a,b)
