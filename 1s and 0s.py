# Python program to print all possible combination of 0s and 1s
def bi(n):
    if n < 1:
        #print("Calling Bi[",0,"]")
        print(A)
    else:
        #print("Calling 1st Bi[",n-1,"]")
        A[n-1] = 0
        bi(n-1)
        #print("Calling 2nd Bi[",n-1,"]")
        A[n-1] = 1
        bi(n-1)
n = int(input())
A  = [0]*n
bi(n)
