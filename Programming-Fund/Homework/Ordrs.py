orders = int(input())
total = 0
for orders in range(0, orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 1 <= days <= 31 and 1 <= capsules <= 2000 and 0.01 <= price <= 100:
        result = price * days * capsules
        total += result
        print(f'The price for the coffee is: ${result:.2f}')
print(f'Total: ${total:.2f}')