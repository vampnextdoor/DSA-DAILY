class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        bucket=[[] for _ in range(len(nums)+1)]
        for num,count in freq.items():
            bucket[count].append(num)
        result=[]
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result)== k:
                    return result

        
       
        
# 347. Top K Frequent Elements
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]