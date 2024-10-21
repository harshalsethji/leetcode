class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        for i in range(k):
            if not max_heap:
                break
            max_gifts = -heapq.heappop(max_heap)
            remaining = int(max_gifts ** 0.5)
            heapq.heappush(max_heap, -remaining)

        total_remaining = -sum(max_heap)
        return total_remaining
