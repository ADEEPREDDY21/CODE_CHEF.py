# Alice and Bob are playing a game of table tennis where irrespective of the point scored, every player makes 
# 2 consecutive serves before the service changes. Alice makes the first serve of the match. Therefore the first 
# 2 serves will be made by Alice, then the next 2 serves will be made by Bob and so on.

# Let's consider the following example match for more clarity:

# Alice makes the 1st serve.
# Let us assume, Bob wins this point. (Score is 0 for Alice and 1 for Bob)
# Alice makes the 2nd  serve.
# Let us assume, Alice wins this point. (Score is 1 for Alice and 1 for Bob)
# Bob makes the 3rd  serve.
# Let us assume, Alice wins this point. (Score is 2 for Alice and 1 for Bob)
# Bob makes the 4th  serve.
# Let us assume, Alice wins this point. (Score is 3 for Alice and 1 for Bob)
# Alice makes the 5th serve.
# And the game continues 
# …
# After the score reaches P and Q for Alice and Bob respectively, both the players forgot whose serve it is. Help them determine whose service it is.

# Input Format
# The first line contains a single integer T — the number of test cases. Then the test cases follow.
# The first line of each test case contains two integers P and Q — the score of Alice and Bob respectively.
def find_serve(t):
  for r in range(t):
    p,q=map(int,input().split())
    total=p+q
    index=total//2
    if index % 2==0:
      print("ALICE")
    else:
      print("BOB")


t=int(input())
find_serve(t)









