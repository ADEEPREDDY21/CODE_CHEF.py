# It's the sale season again and Chef bought items worth a total of X rupees. The sale season offer is as follows:

# if X≤100, no discount.
# if 100<X≤1000, discount is 25 rupees.
# if 1000<X≤5000, discount is 100 rupees.
# if X>5000, discount is 500 rupees.
# Find the final amount Chef needs to pay for his shopping.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of single line of input containing an integer X.
def sale(x):
    if x<100:
        return x
    elif 100<x<=1000:
        return x-25
    elif 1000<x<=5000:
        return x-100
    else:
        return x-500
t=int(input())

for r in range(t):
    x=int(input())
    print(sale(x))
