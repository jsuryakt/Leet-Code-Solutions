class Solution:
 
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        sett = set()
        for word in words:
            res = ""
            for ele in word:
                res += map[ord(ele)-97]
            sett.add(res)
        return len(sett)