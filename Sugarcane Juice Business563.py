# While Alice was drinking sugarcane juice, she started wondering about the following facts:

# The juicer sells each glass of sugarcane juice for 50 coins.
# He spends 20% of his total income on buying sugarcane.
# He spends 20% of his total income on buying salt and mint leaves.
# He spends 30% of his total income on shop rent.
# Alice wonders, what is the juicer's profit (in coins) when he sells N glasses of sugarcane juice?

# Input Format
# The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains an integer N, as described in the problem statement.
def sugarcane(n):
    total=n*50
    a=total*0.2
    b=total*0.2
    c=total*0.3
    d=total-(a+b+c)
    return d
t=int(input())    
for r in range(t):
    n=int(input())
    print(int(sugarcane(n)))
