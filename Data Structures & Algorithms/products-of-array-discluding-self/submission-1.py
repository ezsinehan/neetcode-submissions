class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        length = len(nums)
        
        for i in range(length):
            prod = 1
            for j in range(length):
                if i != j:
                    prod *= nums[j]
            output[i] = prod
        return output

