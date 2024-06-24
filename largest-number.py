from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Custom comparator to sort the numbers
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        nums = list(map(str, nums))
        
        nums.sort(key=cmp_to_key(compare))
        
        largest_num = ''.join(nums)
        
        if largest_num[0] == '0':
            return '0'
        
        return largest_num
