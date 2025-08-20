class Solution(object):
    def zeroFilledSubarray(self, nums):
        counter=0
        subarr=0
        for i in nums:
            if i ==0:
                counter+=1
                subarr+= counter
            else:
                counter=0
        return subarr
        
# 2348. Number of Zero-Filled Subarrays
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
# Example 2:

# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.