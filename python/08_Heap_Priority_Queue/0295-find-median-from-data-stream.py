"""

295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is 
even, there is no middle value, and the median is the mean of the two middle values.

• For example, for arr = [2,3,4], the median is 3.
• For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

• MedianFinder() initializes the MedianFinder object.
• void addNum(int num) adds the integer num from the data stream to the data structure.
• double findMedian() returns the median of all elements so far. Answers within 10-5 of 
  the actual answer will be accepted.
 


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

"""

# Solution 2: Heap [✔️]
# Time Complexity: O(m * log n) for addNum(), O(m) for findMedian().
# Space Complexity: O(n)

# Where m is the number of function calls and n is the length of the array.

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # type: ignore

        # make sure every num small is <= every num in large
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small) # type: ignore
            heapq.heappush(self.large, val) # type: ignore

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small) # type: ignore
            heapq.heappush(self.large, val) # type: ignore
        if len(self.large) > len(self.small) + 1: 
            val = heapq.heappop(self.large) # type: ignore
            heapq.heappush(self.small, -1 * val) # type: ignore

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2