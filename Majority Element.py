class Solution:
    def majorityElement(self, lst):
        map={}
        for i in lst:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        res = max(map,key=lambda key:map[key])
        return res