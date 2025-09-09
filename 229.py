class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        can1, can2 , count1, count2 = None, None, 0, 0 
        for num in nums:
            if can1 == num:
                count1 += 1
            elif can2 == num:
                count2 += 1 
            elif count1 == 0:
                can1, count1 = num, 1
            elif count2 == 0:
                can2, count2 = num, 1 
    
            else:
                count1 -= 1
                count2 -= 1

        result=[]
        n = len(nums)
        for c in [can1,can2]:
            if c is not None and nums.count(c) > n // 3: 
                result.append(c)
        return result
    
# 229. Majority Element II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]