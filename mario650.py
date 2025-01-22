"""Mario's bullet moves at 
X pixels per frame. He wishes to shoot a goomba standing 
Y pixels away from him. The goomba does not move.

Find the minimum time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after at least 
Z seconds from now."""
"""
Input Format
The first line of input will contain an integer 
T, the number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing three space-separated integers 
X,Y and Z."""
for r in range(int(input())):
  x,y,z=map(int,input().split())
  t=int(y/x)#time equal to distance by speed
  print(max(0,z-t))
  
