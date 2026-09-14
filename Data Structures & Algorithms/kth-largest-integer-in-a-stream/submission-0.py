import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        self.hq = [x for x in self.stream ]
        heapq.heapify(self.hq)

        

    def add(self, val: int) -> int:
        if val is not None and self.stream is not None:
            heapq.heappush(self.hq, val)
            res = heapq.nlargest(self.k, self.hq)
            return res[-1]

