prices=(map(int, input().split()))
min_price=float('inf')
max_prof=0
        
for price in prices:
    if price < min_price:
        min_price=price
    elif price-min_price>max_prof:
        max_prof=price-min_price
                
print(max_prof)
