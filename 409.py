import collections
class Solution(object):
    def longestPalindrome(self, s):
        counts=collections.Counter(s)
        longest=0
        oddCenter= False

        for count in counts.values():
            longest+= (count//2)*2
            if count % 2 == 1:
                oddCenter=True
        if oddCenter:
            longest+=1
        return longest 

# 409. Longest Palindrome
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.