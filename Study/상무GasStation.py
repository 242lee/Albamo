class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        tank = 0
        diffsum = 0
        index = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            diffsum += gas[i] - cost[i]
            if tank < 0 :
                tank = 0
                index = i + 1
        return index if index < n and diffsum>= 0 else - 1