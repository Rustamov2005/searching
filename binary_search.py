import time
from datetime import datetime

data = list(set([1, 1, 6, 13, 14, 14, 23, 23, 26, 26, 30, 31, 32, 32, 37, 42, 44, 47, 48, 50]))


data_l = len(data) - 1
data.sort()
print(data)

target = int(input("Target: "))
low = 0
data_l = len(data) - 1
count = 0
print(datetime.now())
while True:
    time.sleep(1)
    count += 1
    middle = (data_l + low) // 2
    if data[middle] < target:
        low = middle + 1
    elif data[middle] == target:
        print(target)
        print(f"qadam = {count}")
        break

    else:
        data_l = middle

print(datetime.now())


# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# print(datetime.now())
#
#
# arr = [0, 1, 2, 4, 9]
# target = 9
# result = binary_search(arr, target)
# if result != -1:
#     print(f"Element {target} indeksi: {result}")
#     print(datetime.now())
# else:
#     print(f"Element {target} topilmadi")
