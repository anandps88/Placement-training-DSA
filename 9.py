n=int(input())
a=[]
c=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b[0])
    c.append(b[1])
print(int(sum(a)/n), int(sum(c)/n))
    
