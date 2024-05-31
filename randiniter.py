import random


data = []
for i in range(10):
    data.append(random.randint(1, 50))
print(data)
target = int(input("target="))
count = 0
for j in data:
    count += 1
    if j == target:
        print(target)
        break

print(count)
