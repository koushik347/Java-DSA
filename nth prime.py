def is_prime(n1):
    if n1<2:
        return False
    for i in range(2,n1+1):
        if n1%i==0:
            return False
        return True
def n_prime(n):
    count=0
    n1=1
    while count<n1:
        n1+=1
        if is_prime(n1):
            count+=1
        return count
n=int(input())