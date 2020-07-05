"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3380/

"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = 0
        i3 = 0
        i5 = 0
        multiple_of_2 = 2
        multiple_of_3 = 3
        multiple_of_5 = 5
        ugly = [0]*n
        ugly[0] = 1
        next_ugly = 1
        
        for i in range(1,n):
            next_ugly = min(multiple_of_2,multiple_of_3,multiple_of_5)
            ugly[i] = next_ugly
            if next_ugly == multiple_of_2:
                i2 = i2+1
                multiple_of_2 = ugly[i2] * 2
            if next_ugly == multiple_of_3:
                i3 = i3+1
                multiple_of_3 = ugly[i3] * 3
            if next_ugly == multiple_of_5:
                i5 = i5+1
                multiple_of_5 = ugly[i5] * 5
        return next_ugly
                