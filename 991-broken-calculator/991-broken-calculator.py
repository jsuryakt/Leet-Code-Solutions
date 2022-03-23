class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while(target>startValue):
            if target%2 == 0:
                target = target//2
            else:
                target += 1
            ans += 1
        return ans + startValue-target