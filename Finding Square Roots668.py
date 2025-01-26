"""
In olden days finding square roots seemed to be difficult but nowadays it can be easily done using in-built functions available across many languages.
Assume that you happen to hear the above words and you want to give a try in finding the square root of any given integer using in-built functions. So here's your chance.
Input
The first line of the input contains an integer T, the number of test cases. T lines follow. Each line contains an integer N whose square root needs to be computed.
"""
import math#by taking in built in function (math) we can perform any math related programs
t=int(input(Enter number of test cases))#taking input from the user to now number of test cases
for r in range(t):
  n=int(input("Enter number to check its square root"))
  square_root=math.sqrt(n)
  print(round(square_root))
