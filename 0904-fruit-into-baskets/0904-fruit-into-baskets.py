class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length = 0
        my_disct = {}
        left = 0
        right = 0
        n = len(fruits)
        while right < n:
            my_disct[fruits[right]] = my_disct.get(fruits[right],0)+1
            if len(my_disct) >2:
                my_disct[fruits[left]]-=1
                if my_disct[fruits[left]] == 0:
                    del my_disct[fruits[left]]
                left +=1
            if len(my_disct) <=2:
                max_length = max(max_length, right- left +1) 
            right +=1
        return max_length           
                     

