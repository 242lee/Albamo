# 134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        ans = tank = 0
        for i in range(len(gas)):
            if tank + gas[i] < cost[i]:
                ans = i + 1     # ans is always < len(gas)
                tank = 0
            else:
                tank += gas[i] - cost[i]

        return ans

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# gas = [2,3,4]
# cost = [3,4,3]
a = Solution()
print(a.canCompleteCircuit(g,s))