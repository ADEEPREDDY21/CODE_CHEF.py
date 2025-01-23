"""You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S contains the character A,T,Cand G only.
Chef knows that:
A is complementary to T.
T is complementary to A.
C is complementary to G.
G is complementary to C.
Using the string S, determine the sequence of the complementary strand of the DNA.
Input Format
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case contains an integer N - denoting the length of string S.
Second line contains N characters denoting the string S."""
for r in range(int(input())):
    n=int(input())
    s=input()
    new_string=""
    for c in s:
        if c=="A":
            new_string+="T"
        elif c=="T":
            new_string+="A"
        elif c=="C":
            new_string+="G"
        elif c=="G":
            new_string+="C"
        else:
            print("hi")
    print(new_string)        
