# // Time Complexity : O(n) 
# // Space Complexity : O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = nums[0]
        output = [i for i in nums]

        for i in range(1,len(nums)):
            output[i] = prod
            prod *= nums[i]

        
        prod = nums[-1]  
        output[0] = 1
        for i in range(len(nums)-2, -1, -1):
            output[i] = output[i] * prod
            prod *= nums[i] 

        return(output)