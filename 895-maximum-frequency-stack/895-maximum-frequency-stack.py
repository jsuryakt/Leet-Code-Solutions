from heapq import heappop, heappush, heapify

class FreqStack:
    
    class Pair:
        def __init__(self, val, ele, pos):
            self.val = val
            self.ele = ele
            self.pos = pos
            
        def __lt__(self, other):
            if self.val == other.val:
                return self.pos > other.pos
            return self.val < other.val
        
        def __str__(self):
            return "{}-{},".format(-1 * self.val, self.ele)

    def __init__(self):
        self.freqDic = {}
        self.maxHeap = []
        self.idx = 0
        heapify(self.maxHeap)

    def push(self, val: int) -> None:
        self.freqDic[val] = self.freqDic.get(val, 0) + 1
        heappush(self.maxHeap, self.Pair(-1 * self.freqDic[val], val, self.idx))
        self.idx += 1
        

    def pop(self) -> int:
        # print(self.freqDic)
        heapTop = heappop(self.maxHeap)
        element, pos = heapTop.ele, heapTop.pos
            
        self.freqDic[element] = self.freqDic[element]-1
        
        return element