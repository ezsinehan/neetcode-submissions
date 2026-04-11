class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        # middle = len(nums) // 2
        right  = len(nums) - 1

        # goal is to shrink array till we reach the potential location of our number
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle   
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1