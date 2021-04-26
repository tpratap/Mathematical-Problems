# Generating all possible valid combinations of parenthesis using Python
def check(A):
    c = 0
    o = 0
    #print(len(A))
    for i in range(len(A)):
        if c > o:
            return -1
        elif A[i] == '(':
            o += 1
        elif A[i] == ')':
            c += 1
    if c == o:
        return 1
def display(A):
    for i in range(len(A)):
        print(A[i],end = "")
    print()
def bi(n):
    if n < 1:
        if check(A) == 1:
            display(A)
    else:
        A[n-1] = ('(')
        bi(n-1)
        A[n-1] = (')')
        bi(n-1)
k = int(input())
A =['(',')']*k
bi(2*k)
