a=input().split()
n=int(a[0])
k=int(a[1])
b=[]
c=input().split()
b = [int(x) for x in c]
maxkick=0
for i in range(k):
    maxkick=max(maxkick,b[i])
print(maxkick)
curr=b[0:k]
for i in range(k,n):
    curr.pop(0)
    curr.append(b[i])
    maxkick=max(curr)
    print(maxkick)