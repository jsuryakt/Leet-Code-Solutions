class Solution:
    def getFilesAndContent(self, string, dic):
        content = re.findall("\(([^ ]*)\)", string)
        files = re.sub("\([^ ]*\)", "", string)
        splitFiles = files.split(" ")

        base = splitFiles[0]
        for i in range(1, len(splitFiles)):
            key = content[i-1]
            value = base+"/"+splitFiles[i]
            if key in dic:
                dic[key].append(value)
            else:
                dic[key] = [value]
        return dic
        
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for str in paths:
            dic = self.getFilesAndContent(str, dic)
        ans = []
        for key in dic:
            lst = dic[key]
            if(len(lst)>1):
                ans.append(lst)
        return ans