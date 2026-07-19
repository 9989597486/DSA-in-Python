import heapq

numbers = [20, 10, 30, 5]

heapq.heapify(numbers)

print(numbers)

heapq.heappush(numbers, 2)

print(numbers)

print(heapq.heappop(numbers))
