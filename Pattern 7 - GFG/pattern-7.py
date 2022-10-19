#User function Template for python3

class Solution:
    def printTriangle(self, N):
        stars = 1
# giv odd no only
        total = N
        for i in range(total):
            spaces = (total*2)-stars
            for _ in range(spaces//2):
                print(" ", end="")
            for _ in range(stars):
                print("*", end="")
            for _ in range(spaces//2):
                print(" ", end="")
            stars += 2
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends