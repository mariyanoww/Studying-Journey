numbers = list(map(int, input().split()))
chislo = int(input())
for ilian in range(0, chislo):
    numbers.remove(min(numbers))
print(', '.join(map(str, numbers)))
