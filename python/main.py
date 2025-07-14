# import heapq

# minHeap = []
# heapq.heappush(minHeap, 3)
# heapq.heappush(minHeap, 2)
# heapq.heappush(minHeap, 4)

# print(minHeap[0])

# while len(minHeap):
#     print(heapq.heappop(minHeap))

def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))