#User function Template for python3

class Solution:
    def printTriangle(self, N):
        stars = 1
        for i in range(N):
            spaces = (N*2)-stars
            for _ in range(spaces//2):
                print(" ", end="")
            for _ in range(stars):
                print("*", end="")
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