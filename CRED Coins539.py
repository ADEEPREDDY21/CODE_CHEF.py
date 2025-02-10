# For each bill you pay using CRED, you earn X CRED coins.
# At CodeChef store, each bag is worth 100 CRED coins.

# Chef pays Y number of bills using CRED. Find the maximum number of bags he can get from the CodeChef store.

# Input Format
# First line will contain T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers X and Y.
for r in range(int(input())):
    x,y=map(int,input().split())
    coins=x*y
    total=coins//100
    print(total)
