# There are 4 companies in the markets of Chefland, A,B,C and D.
# This year,Company A made a profit of P lakh rupees,
# Company B made a profit of Q lakh rupees,
# Company C made a profit of R lakh rupees,
# Company D made a profit of S lakh rupees.
# There is said to be a monopoly in the market if the profit made by one company is strictly greater than the sum of profits made by all other companies.
# Determine if there is a monopoly in the market or not.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# The first line and only line of each test case contains four space-separated integers P,Q,R and S — the profits made by companies A,B,C and D respectively.
def monopoly(a,b,c,d):
    if a>(b+c+d) or b>(a+c+d) or c>(a+b+d) or d>(a+b+c):
        return "YES"
    else:
        return "NO"
t=int(input())        
for r in range(t):
    p,q,r,s=map(int,input().split())
    print(monopoly(p,q,r,s))
