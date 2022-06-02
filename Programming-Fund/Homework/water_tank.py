tank = 0
lines = int(input())
for a in range(0, lines):
    fill = int(input())
    tank += fill
    if tank > 255:
        print('Insufficient capacity!')
        tank -= fill
    else:
        continue
print(tank)
