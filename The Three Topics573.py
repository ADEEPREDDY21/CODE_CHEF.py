# The Chef has reached the finals of the Annual Inter-school Declamation contest.

# For the finals, students were asked to prepare 10 topics. However, Chef was only able to prepare three topics, numbered A,B and C 
# — he is totally blank about the other topics. This means Chef can only win the contest if he gets the topics A,B or C to speak about.

# On the contest day, Chef gets topic X. Determine whether Chef has any chances of winning the competition.

# Print "Yes" if it is possible for Chef to win the contest, else print "No".

# You may print each character of the string in either uppercase or lowercase (for example, the strings yEs, yes, Yes, and YES will all be treated as identical).

# Input Format
# The first and only line of input will contain a single line containing four space-separated integers A, B ,C and 
# X — the three topics Chef has prepared and the topic that was given to him on contest day.
def topics(a,b,c,d):
    if a==d or b==d or c==d:
        return "YES"
    else:
        return "NO"

w,x,y,z=map(int,input().split())
print(topics(w,x,y,z))    
