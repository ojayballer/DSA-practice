import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1 :
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            
            if a != b :
                diff = a - b 
                heapq.heappush(stones,diff)
        
        
        if not stones :
            return 0 
        
        return abs(stones[0])