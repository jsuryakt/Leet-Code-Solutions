class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        ans = []
        
        length = len(s)
        for i in range(length):
            lastIndex[s[i]] = i
            
        start = 0
        while(start<length):
            count = 0
            end = lastIndex[s[start]]
            while(start<=end):
                if(lastIndex[s[start]] > end):
                    end=lastIndex[s[start]]
                start += 1
                count += 1
            ans.append(count)
        
        return ans