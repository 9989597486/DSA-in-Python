numbers = [2, 4, 6, 8, 10, 12]

key = 10

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == key:
        print("Element Found")
        break
    elif numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
