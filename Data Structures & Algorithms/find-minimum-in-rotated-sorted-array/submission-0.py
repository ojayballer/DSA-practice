class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()  #O(n)
        return nums[0]

        