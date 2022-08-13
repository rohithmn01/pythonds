import heapq
import ipdb
def heapreplace_max(heap, item):
    heap[0] = item
    heapq._siftup_max(heap, 0)



def minsum(nums,k):
    heap = nums
    heapq._heapify_max(heap)
    print(heap)
    for i in range(k):
        max_value = heap[0]
        heapreplace_max(heap, max_value//2)
        print(heap)
    return sum(heap)



nums=[10,20,7]
k=4
res = minsum(nums,k)
print(res)
