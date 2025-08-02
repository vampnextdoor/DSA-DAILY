class Solution(object):
    def sortArray(self, nums):
        def heapify(arr,n,i):
            largest=i
            left=2*i+1
            right=2*i+2
            if left<n and arr[left]>arr[largest]:
                largest=left
            if right<n and arr[right]>arr[largest]:
                largest=right
            if largest !=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                heapify(arr,n,largest)
        n=len(nums)
        for i in range(n // 2-1,-1,-1):
            heapify(nums,n,i)
        for i in range(n-1,0,-1):
            nums[0],nums[i]=nums[i],nums[0]
            heapify(nums,i,0)
        return nums

# Sort an Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).