def markFalse(a,n):
    p=2*a+3
    start = (p*p - 3) // 2
    for k in range(start,size,p):
        isPrime[k]=False

n=int(input())
primes=[2]
size=int(0.5*(n-3)+1)
isPrime=[True]*size

for i in range(size):
    if isPrime[i]:
        primes.append(2*i+3)
        markFalse(i,n)
print(primes)