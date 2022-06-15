def odd_and_even(receive):
    odd_sum = 0
    even_sum = 0
    for x in receive:
        if x % 2 == 0:
            even_sum += x
        else:
            odd_sum += x
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(odd_and_even(list(map(int, input()))))
