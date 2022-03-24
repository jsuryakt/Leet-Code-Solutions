class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1,2,2,3
        people.sort()
        l = 0
        r = len(people)-1
        boat = 0
        while(l<=r):
            summ = people[l]+people[r]
            if summ <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boat += 1
        return boat