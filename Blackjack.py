# Chef is playing a variant of Blackjack, where 3 numbers are drawn and each number lies between 1 and 10 (with both 1 and 10 inclusive). Chef wins the game when the sum of these 
# 3 numbers is exactly 21.
# Given the first two numbers A and B, that have been drawn by Chef, what should be 3-rd number that should be drawn by the Chef in order to win the game?

# Note that it is possible that Chef cannot win the game, no matter what is the 3-rd number. In such cases, report −1 as the answer.
# Input Format
# The first line will contain an integer T - number of test cases. Then the test cases follow.
# The first and only line of each test case contains two integers A and B - the first and second number drawn by the Chef.
t=int(input())
for r in range(t):
  a,b=map(int,input().split())
  s=a+b
  c=21-s
  if 1<=c and c<=10:
    print(c)
  else:
    print(-1)
