class Solution:
    def factorial(self,n):
        ans = 1
        for i in range(1,n+1):
            ans = ans*i
        return ans
    
    def countOrders(self, n: int) -> int:
        order = n
        totalSpaces = order*2
        
        finalAns = self.factorial(order)%(10**9+7)
        for i in range(1, order+1):
            finalAns = (finalAns * ((order-i)*2 + 2 - 1))%(10**9+7)
        return finalAns%(10**9+7)
            