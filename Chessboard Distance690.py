"""
The Chessboard Distance between any two points 
(𝑋1,𝑌1)(X1​ ,Y1​ )and (𝑋2,𝑌2)(X2 ,Y2​ ) on a Cartesian plane is defined as 
max(∣𝑋1−𝑋2∣,∣𝑌1−𝑌2∣). You are given two points (𝑋1,𝑌1) and (𝑋2,𝑌2)
Output their Chessboard Distance.
Note that ∣𝑃∣ denotes the absolute value of integer P, e.g.,∣−4∣=4 and ∣7∣=7. Input Format: The first line contains 
𝑇, the number of test cases. Then, T test cases follow. Each test case consists of a single line of input containing four space-separated integers: 
𝑋1,𝑌1,𝑋2,𝑌2 , as defined in the problem statement.
"""
for r in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    x=abs(x1-x2)
    y=abs(y1-y2)
    print(max(x,y))
