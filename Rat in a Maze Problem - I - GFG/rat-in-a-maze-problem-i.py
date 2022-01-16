#User function Template for python3

class Solution:
    ans = []
    def createGraph(self,m, n):
        graph = []
        count = 0
        for i in range(n):
            for j in range(n):
                if m[i][j] == 1:
                    lst = [-1,-1,-1,-1]
                    # Left
                    if(j>0 and m[i][j]==m[i][j-1]):
                        lst[0] = count-1
                    
                    # Right
                    if(j+1<n and m[i][j]==m[i][j+1]):
                        lst[1] = count + 1
                    
                    # Top
                    if(i>0 and m[i][j]==m[i-1][j]):
                        lst[2] = count - n
                    
                    # Bottom    
                    if(i+1<n and m[i][j]==m[i+1][j]):
                        lst[3] = count + n
                    
                    graph.append(lst)
                else:
                    graph.append(-1)
                    
                count += 1
        return graph
        
    def getDirection(self,i):
        if i == 0:
            return 'L'
        elif i == 1:
            return 'R'
        elif i == 2:
            return 'U'
        else:
            return 'D'
        
    def printAllPaths(self,src, graph, n, possible, visited):
        # global ans
        if src == (n*n - 1):
            self.ans.append(possible)
            return 
        
        visited[src] = True
        
        if graph[src] != -1:
            for i in range(4):
                neighbor = graph[src][i]
                if neighbor != -1 and visited[neighbor] == False:
                    direction = self.getDirection(i)
                    self.printAllPaths(neighbor, graph, n, possible+direction, visited)
                    
        visited[src] = False
        
    def findPath(self, m, n):
        # global ans
        self.ans = []
        graph = self.createGraph(m, n)
        visited = [False]*(n*n)
        self.printAllPaths(0, graph, n, "", visited)
        return self.ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends