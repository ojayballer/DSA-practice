class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()  # O(nlogn)
        return nums[0]  