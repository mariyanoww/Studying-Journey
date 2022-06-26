visits = int(input())
visits_made = 0
total = 0
while visits_made < visits:
    visits_made += 1
    city_name = input()
    income = float(input())
    expenses = float(input())
    if visits_made % 5 == 0:
        income = income * 0.90
    elif visits_made % 3 == 0:
        expenses = expenses * 1.50
    income -= expenses
    total += income
    print(f'In {city_name} Burger Bus earned {income:.2f} leva.')
print(f"Burger Bus total profit: {total:.2f} leva.")
