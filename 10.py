nums=list(map(int, input().split()))
c=0
for num in nums:
    if c==0:
        maj=num
    c+=(1 if num==maj else -1)

print(maj)