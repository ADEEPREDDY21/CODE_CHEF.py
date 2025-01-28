'''
Chef received N candies on his birthday. He wants to put these candies in some bags. A bag has 
K pockets and each pocket can hold at most M candies. Find the minimum number of bags Chef needs 
so that he can put every candy into a bag.
Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line containing three space-separated integers N,K,M
Key Points
Each bag has:
K: Number of pockets.
M: Maximum candies a single pocket can hold.
Therefore, a single bag can hold up to 𝐾×𝑀candies.
Chef has N candies in total and wants to distribute them in the minimum number of bags.

Steps to Solve
Calculate the Capacity of One Bag:

The total number of candies a single bag can hold is:
Capacity of one bag=𝐾×𝑀
Determine the Number of Bags Needed:

To find the minimum number of bags needed:
Bags required=⌈𝑁 /Capacity of one bag⌉
Since we cannot have a fraction of a bag, we use the ceiling function to round up.

In integer arithmetic (to avoid using the ceiling function):

Bags required=𝑁+Capacity of one bag−1/Capacity of one bag
This formula ensures that any remainder is accounted for by rounding up.'''
t=int(input())
for r in range(t):
  n,k,m=map(int,input().split())
  total=k*m
  result=(n+(total-1))//total
  print(result)
  
