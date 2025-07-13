a=input().split()
n,k=int(a[0]),int(a[1])
b=[]
c=input().split()
b = [int(x) for x in c]
maxsum=0
for i in range(k):
    maxsum+=b[i]
sum=0
for i in range(k,n):
    sum=maxsum+b[i]-b[i-k]
    maxsum=max(maxsum,sum)
print(maxsum)   
