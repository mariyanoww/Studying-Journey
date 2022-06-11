course = 0
people = int(input())
capacity = int(input())
passed = 0
while True:
    if passed >= people:
        print(course)
        break
    elif passed < people:
        passed += capacity
        course += 1
        continue
