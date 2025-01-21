"""Mario and Transformation
Mario transforms each time he eats a mushroom as follows:

If he is currently small, he turns normal.
If he is currently normal, he turns huge.
If he is currently huge, he turns small.
Given that Mario was initially normal, find his size after eating 
X mushrooms.

Input Format
The first line of input will contain one integer 
T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, containing one integer X."""


for r in range(int(input())):
  x=int(input())
  a=x%3
  if a>=0:
    if a==0:
      print("NORMAL")
    elif a==1:
      print("HUGE")
    else:
      print("SMALL")
