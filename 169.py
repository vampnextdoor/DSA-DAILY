class Solution(object):
    def majorityElement(self, nums):
        candidate=0
        count=0
        for i in nums:
            if count==0:
                candidate=i
                count=1
            elif i==candidate:
                count+=1
            else:
                count-=1
        return candidate
    
#     169. Majority Element
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2