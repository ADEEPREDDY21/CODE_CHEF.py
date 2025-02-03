# Chef is a very big fan of Eren Yeager.

# In the last season of Attack on Titan, there were N episodes numbered from 1 to N.
# Each even indexed episode was A minutes long and each odd indexed episode was B minutes long.
# Calculate the total duration (in minutes) of the last season.

# Input Format
# The first line of input contains a single integer T, the number of test cases.
# The first and only line of each test case contains three integers N ,A, and B
# the number of episodes and the durations of each even-indexed and odd-indexed episodes respectively in minutes.
for r in range(int(input())):
  def eren(n,a,b):
    count_a=0
    count_b=0
    for r in range(1,n+1):
      if r%2==0:
        count_a += a
      else:
        count_b += b
    return count_a + count_b
n,a,b=map(int,input().split())
result=eren(n,a,b)
print(result)
