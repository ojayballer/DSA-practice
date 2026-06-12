class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = set()
        for num in nums :
            
            if num in hash :
                hash.remove(num)
            else :
                hash.add(num)
            
            
        return hash.pop()
            