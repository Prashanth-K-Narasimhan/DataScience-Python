import heapq
heap = []
heapq.heappush(heap, (5, 'write code'))
heapq.heappush(heap, (7, 'release product'))
heapq.heappush(heap, (1, 'write spec'))
heapq.heappush(heap, (3, 'create tests'))
print(heapq.heappop(heap))#pops smallest
print(heapq.nlargest(2,heap))#displays n largest values without popping
print(heapq.nsmallest(2,heap))#displays n smallest values without popping
print(heap)
heap = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(heap)#converts a list to heap
print(heap)
def heapsort(iterable):
     h = []
     for value in iterable:
         heapq.heappush(h, value)
     return [heapq.heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])