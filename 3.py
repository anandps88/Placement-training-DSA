def count_zeroes(n):
    count=0
    l=len(str(n))-1
    m=l
    while(m>1):
         count+=9*(m-1)*10**(m-2)
         m-=1
    for i in range(10**l,n+1):
         count += str(i).count('0')
    return count
n = int(input())
print(count_zeroes(n))