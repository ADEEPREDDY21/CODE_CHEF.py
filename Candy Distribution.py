"""
Candy Distribution
Chef has N candies. He has to distribute them to exactly 
M of his friends such that each friend gets equal number 
of candies and each friend gets even number of candies. 
Determine whether it is possible to do so.

NOTE: Chef will not take any candies himself and will distribute all the candies.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers N and M, 
the number of candies and the number of friends.
"""
t=int(input("Enter number of test cases"))
for r in range(t):
  n,m=map(int,input().split())
  if n%2==0 and n%m==0:
    print("YES")
  elif m==0:
    print("NO")
  else:
    print("NO")
