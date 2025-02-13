# In Chefland, a tennis game involves 4 referees.
# Each referee has to point out whether he considers the ball to be inside limits or outside limits. The ball is considered to be IN if and only if all the referees agree that it was inside limits.

# Given the decision of the 4 referees, help Chef determine whether the ball is considered inside limits or not.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of a single line of input containing 4 integers R1​ ,R2 ,R3 ,R4  denoting the decision of the respective referees.
# Here R can be either 0 or 1 where 0 would denote that the referee considered the ball to be inside limits whereas 1 denotes that they consider it to be outside limits.
def chefland(r1,r2,r3,r4):
    if r1==0 and r2==0 and r3==0 and r4==0:
        return "IN"
    else:
        return "OUT"
t=int(input())        
for r in range(t):
    a,b,c,d=map(int,input().split())
    print(chefland(a,b,c,d))
  #alternative way
def codechef(referees):
    return "In" if max(referees)==0 else "OUT" 
t=int(input())    
for r in range(t):
    referees=list(map(int,input().split()))
    print(codechef(referees))
