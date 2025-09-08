class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0 
        current_sum = 0
        prefix_sum = {0: 1}  # To handle subarrays starting at index 0
        
        for num in nums:
            current_sum += num
            difference = current_sum - k
            count += prefix_sum.get(difference, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count

# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2