#!/bin/python3

def fb(n):
	
  if n % 3 == 0:	   
    if n % 5 == 0: 
      return "FizzBuzz"
    return "Fizz"
  elif n % 5 == 0:
    return  "Buzz"
  return ""
			
i = 1
while i <= 20:
	print(i, fb(i))
	i = i+1


