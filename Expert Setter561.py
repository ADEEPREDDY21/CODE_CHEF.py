# A problem setter is called an expert if at least 50% of their problems are approved by Chef.

# Munchy submitted X problems for approval. If Y problems out of those were approved, find whether Munchy is an expert or not.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of a two space-separated integers X and Y - the number of problems submitted and the number of problems that were approved by Chef.
def expert(x,y):
    approve=x/2
    if y>=approve:
        return "YES"
    else:
        return "No"
t=int(input())        
for r in range(t):
    x,y=map(int,input().split())
    print(expert(x,y))
