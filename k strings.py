# Printing all possible combinations of k strings for n digits
def K(n,k):
    if n < 1:
        print(A)
    else:
        for i in range(k):
            A[n-1] = i
            K(n-1,k)
k = int(input("Numbers upto (K):"))
n = int(input("No. of digit(n):"))
A  = [0]*n
K(n,k)
