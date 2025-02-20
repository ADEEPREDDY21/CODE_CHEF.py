# Chef wants to reach home as soon as possible. He has two options:

# Travel with his BIKE which takes X minutes.
# Travel with his CAR which takes Y minutes.
# Which of the two options is faster or do they both take same time?

# Input Format
# First line will contain T, number of test cases. Then the test cases follow.
# Each test case contains a single line of input, two integers X,Y representing the time taken to travel with BIKE and CAR respectively.
def travel(a,b):
    if a<b:
        return "BIKE"
    elif a>b:
        return "CAR"
    else:
        return "SAME"
        
t=int(input())

for r in range(t):
    x,y=map(int,input().split())
    print(travel(x,y))
