class Solution:
    def getMorse(self, str):
        map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = ""
        for ele in str:
            res += map[ord(ele)-97]
        return res
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        sett = set()
        for word in words:
            sett.add(self.getMorse(word))
        return len(sett)