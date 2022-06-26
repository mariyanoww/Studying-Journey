price_ratings = input()
entry_point = int(input())
command = input()
price_ratings = price_ratings.split(", ")
price_rating = [int(x) for x in price_ratings]
sum_left = 0
sum_right = 0
left_list = price_rating[:entry_point]
right_list = price_rating[entry_point + 1:]
entry_point = price_rating.pop(entry_point)
for x in left_list:
    if command == "cheap":
        if x < entry_point:
            sum_left += x
    else:
        if x >= entry_point:
            sum_left += x
for x in right_list:
    if command == "cheap":
        if x < entry_point:
            sum_right += x
    else:
        if x >= entry_point:
            sum_right += x
if sum_left >= sum_right:
    print(f"Left - {sum_left}")
elif sum_right > sum_left:
    print(f"Right - {sum_right}")

