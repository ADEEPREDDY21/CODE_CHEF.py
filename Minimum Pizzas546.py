# Each pizza consists of 4 slices. There are N friends and each friend needs exactly X slices.

# Find the minimum number of pizzas they should order to satisfy their appetite.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two integers N and X, the number of friends and the number of slices each friend wants respectively.
def pizza(n,x):
    total=n*x
    pizzas=(total+3)//4
    return pizzas
t=int(input())#test case input
for r in range(t):
    a,b=map(int,input().split())
    print(pizza(a,b))
 
