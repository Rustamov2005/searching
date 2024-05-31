import time
from datetime import datetime

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 12, 20, 13, 19]

colum = int(input("target= "))
count = 0
print(datetime.now())
for i in data:
    time.sleep(1)
    count += 1
    if i == colum:
        print(colum)
        print(datetime.now())
        break
print(count)


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
#
#
# arr = [2, 4, 0, 1, 9]
# target = 1
# result = linear_search(arr, target)
# if result != -1:
#     print(f"Element {target} indeksi: {result}")
# else:
#     print(f"Element {target} topilmadi")
