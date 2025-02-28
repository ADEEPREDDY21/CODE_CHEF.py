# In a coding contest, there are two types of problems:

# Easy problems, which are worth 1 point each
# Hard problems, which are worth 2 points each
# To qualify for the next round, a contestant must score at least X points. Chef solved A Easy problems and B Hard problems. Will Chef qualify or not?

# Input Format
# The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
# Each test case consists of a single line of input containing three space-separated integers — X,A, and B.
def qualify(x,a,b):
    A=1*a
    B=2*b
    total=A+B
    if total>=x:
        return "qualify"
    else:
        return "NotQualify"
t=int(input())
for r in range (t):
    a,b,c=map(int,input().split())
    print(qualify(a,b,c))
