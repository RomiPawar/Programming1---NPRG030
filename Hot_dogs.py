import sys

price_counts = [0] * 5001
for line in sys.stdin:
    for s in line.split():
        price_counts[int(s)] += 1

total_count = 0
max_revenue = 0
max_price = 0
for price in range(5000, 0, -1):
    total_count += price_counts[price]
    if total_count * price >= max_revenue:
        max_revenue = total_count * price
        max_price = price
print(max_price)
