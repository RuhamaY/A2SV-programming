class Solution(object):
    def applyOperations(self, nums):
      
        n = len(nums)
        write_index = 0
        
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[write_index] = nums[i]
                write_index += 1
        
        for i in range(write_index, n):
            nums[i] = 0
        
        return nums
