"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3368/
"""
class Solution:
    def singleNumber(self, nums):
        dic = {}
        for ele in nums:
            dic[ele] = dic.get(ele, 0) + 1
        for k,v in dic.items():
            if v==1:
                return(k)