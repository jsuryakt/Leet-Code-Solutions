class Solution:
    def getNextNeighbors(self, word, wordList, dic):
        allNeighbors = []
        
        charArr = []
        for char in word:
            charArr.append(char)
        
        # ['h','i','t']
        
        for i in range(len(word)):
            old = charArr[i]
            for j in range(26):
                ch = ord('a') + j
                charArr[i] = chr(ch)
                newWord = "".join(charArr)
                # print("neword", newWord)
                if newWord in dic:
                    allNeighbors.append(newWord)
            charArr[i] = old
        # print(allNeighbors)
        return allNeighbors
        
#         for ele in wordList:
#             count = 0
#             for i in range(len(word)):
#                 if word[i] != ele[i]:
#                     count += 1
#                 if count > 1:
#                     break
#             if count == 1 and dic[ele] == False:
#                 allNeighbors.append(ele)

#         return allNeighbors
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = {beginWord: True}
        
        for word in wordList:
            dic[word] = False
        
        if endWord not in dic:
            return 0
        
        queue = []
        ansCount = 1
        
        queue.append(beginWord)
        
        while(queue):
            # print("Queue", ansCount, queue)
            size = len(queue)
            while(size > 0):
                curr = queue.pop(0)
            
                if curr == endWord:
                    return ansCount

                neighbors = self.getNextNeighbors(curr, wordList, dic)


                for neighbor in neighbors:
                    if dic[neighbor] == False:
                        dic[neighbor] = True
                        queue.append(neighbor)
                size -= 1
            ansCount += 1
        return 0
