import heapq
heap = []

'''
            Sample input
            1
            5 3
            8 7 2 6 10
            1 5 8 4 8
'''

heapq.heappush(heap, (8, 1))
heapq.heappush(heap, (7, 5))
heapq.heappush(heap, (2, 8))
heapq.heappush(heap, (6, 4))
heapq.heappush(heap, (10, 8))

# heapq.heappush(heap, (1, 8))
# heapq.heappush(heap, (5, 7))
# heapq.heappush(heap, (8, 2))
# heapq.heappush(heap, (4, 6))
# heapq.heappush(heap, (8, 10))

# heap.reverse()

for i in heap:
    print(heap.pop())

print(heap)