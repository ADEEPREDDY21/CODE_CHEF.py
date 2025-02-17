# You know that 1 kg of pulp can be used to make 1000 pages and 1 notebook consists of 100 pages.

# Suppose a notebook factory receives N kg of pulp, how many notebooks can be made from that?

# Input Format
# First line will contain T, the number of test cases. Then the test cases follow.
# Each test case contains a single integer N - the weight of the pulp the factory has (in kgs).
def notebook(n):
    total=int(n*10)
    return total
t=int(input())
for r in range(t):
    a=int(input())
    print(notebook(a))
