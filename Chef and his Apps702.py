# Chef's phone has a total storage of S MB. Also, Chef has 2 apps already installed on his phone which occupy X MB and Y MB respectively.

# He wants to install another app on his phone whose memory requirement is Z MB.
# For this, he might have to delete the apps already installed on his phone. Determine the minimum number of apps he has to delete from his phone so that he has enough memory to install the third app.

# Input Format
# The first line contains a single integer T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains four integers S,X,Y and Z — the total memory of Chef's phone, the memory occupied by the two already installed apps and the memory required by the third app.
for r in range(int(input())):
    s,x,y,z=map(int,input().split())
    total=x+y
    free_space=s-total
    a=s-x
    b=s-y
    if free_space>=z:
        print(0)
    elif a>=z or b>=z:
        print(1)
    else:
        print(2)
