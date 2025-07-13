a = input().rstrip()

from collections import Counter
counts = Counter(a)
odd_count = sum(1 for v in counts.values() if v % 2 != 0)

if odd_count > 1:
    print("NO")
else:
    print("YES")