# Valentine's Day is approaching and thus Chef wants to buy some chocolates for someone special.

# Chef has a total of X rupees and one chocolate costs Y rupees. What is the maximum number of chocolates Chef can buy?

# Input Format
# First line will contain T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, two integers X,Y - the amount Chef has and the cost of one chocolate respectively.
t=int(input())
for r in range(t):
  x,y=map(int,input().split())
  if x<y:
    print(0)
  else:
    print(x//y)
