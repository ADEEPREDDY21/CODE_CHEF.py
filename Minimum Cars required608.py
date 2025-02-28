# A single car can accommodate at most 4 people.N friends want to go to a restaurant for a party. Find the minimum number of cars required to accommodate all the friends.

# Input Format
# The first line contains a single integer T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains an integer N - denoting the number of friends.
def car(x):
    a=(x+3)//4
    return a
t=int(input())
for r in range(t):
    x=int(input())
    print(car(x))
