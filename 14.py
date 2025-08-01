class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        str1=strs[0]
        str2=strs[-1]
        strc=""
        minlen=min(len(str1),len(str2))
        for i in range(minlen):
            if str1[i]==str2[i]:
                strc+=str1[i]
            else:
                break
        return strc
    
# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"