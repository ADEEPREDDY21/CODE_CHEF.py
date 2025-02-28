# Election season has started in Chefland and the election commission wants to know the count of eligible voters.

# There are N people in Chefland where the age of the ith person in Ai.
# Given that a person needs to be at least X years old to vote, find the number of eligible voters.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of multiple lines of input.The first line of each test case contains two space-separated integers N and X — the number of people in Chefland, and the minimum age required for a person to vote in Chefland.
# The next line contains N space-separated integers, where the ith  integer denotes the age of the ith person.
def voter(n,x,i):
    count=0
    for r in i:
        if r >= x:
            count+=1
        else:
            count+=0
    return count
t=int(input())
for r in range(t):
    n,x=map(int,input().split())
    i=list(map(int,input().split()))
    
    print(voter(n,x,i))
