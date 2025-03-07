# Chef has three water bottles. At any point, if at least two of them are empty, she will fill them up. But if at most one bottle is empty, she will wait, and not fill them up now.

# You are given three integers - B1,B2 and B3.
# If B1=1, it means that the first bottle is full.
# If B1​=0, it means that the first bottle is empty.
# Similarly,B2 denotes whether the second bottle is full or empty, and B3  denotes it for the third bottle.

# Output "Water filling time", if Chef has to fill the bottles now. If not, output "Not now".

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# The only line of each test case contains three space-separated integers,B1​ ,B2​ ,B3
for r in range(int(input())):
    b1,b2,b3=map(int,input().split())
    if b1+b2+b3<2:
        print("Water filling time")
    else:
        print("Not Now")
