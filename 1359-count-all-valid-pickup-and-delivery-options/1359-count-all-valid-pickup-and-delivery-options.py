class Solution: 
    def countOrders(self, n: int) -> int:
        order = n
        totalSpaces = order*2
        
        finalAns = 1
        for i in range(1, order+1):
            finalAns = (finalAns * (2*i - 1)*i)%(10**9+7)
        return finalAns%(10**9+7)
            