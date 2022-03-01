class Solution:
    def countSetBits(self, n):
        count = 0
        while (n):
            n = n & (n-1)
            count+= 1

        return count
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.countSetBits(i))
        return ans