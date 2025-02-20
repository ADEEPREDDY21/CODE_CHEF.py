# There are N children and Chef wants to give them 1 candy each. Chef already has X candies with him. To buy the rest, he visits a candy shop. In the shop, packets containing exactly 
# 4 candies are available.

# Determine the minimum number of candy packets Chef must buy so that he is able to give 1 candy to each of the N children.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# The first and only line of each test case contains two integers N and X — the number of children and the number of candies Chef already has.
import math
def candies(n,x):
    total=(n-x)/4
    if x>=n:
        return 0
    else: 
        return math.ceil(total)

for r in range(int(input())):
    n,x=map(int,input().split())
    print(candies(n,x))

    
