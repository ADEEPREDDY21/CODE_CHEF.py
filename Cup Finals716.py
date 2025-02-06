# Cup Finals
# It is the World Cup Finals. Chef only finds a match interesting if the skill difference of the competing teams is less than or equal to D.

# Given that the skills of the teams competing in the final are X and Y respectively, determine whether Chef will find the game interesting or not.

# Input Format
# The first line of input will contain a single integer T, denoting the number of testcases. The description of T testcases follows.
# Each testcase consists of a single line of input containing three space-separated integers X,Y, and D — the skill levels of the teams and the maximum skill difference.
for r in range(int(input())):
    x,y,d=map(int,input().split())
    diff=abs(x-y)
    if diff<=d:
        print("YES")
    else:
        print("NO")
