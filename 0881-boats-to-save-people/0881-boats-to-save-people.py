class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) -1
        boot = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left +=1
            right -=1
            boot +=1
        return boot        