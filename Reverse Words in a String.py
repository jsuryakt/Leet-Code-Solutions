"""
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.\

https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3391/
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        start = 0
        end = len(lst) - 1
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
        return(" ".join(lst))
    
    #OR
    
    return " ".join(s.split()[::-1])