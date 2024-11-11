class Solution:
    def maxArea(self, height: list[int]) -> int:
        water_list = []
        heights = len(height)
        index = 0
        for water in height:
            water_list.append([water, index])
            index += 1
        
        amount = []
        for water in water_list:
            for compare_water_index in range(water[1], heights):
                water_height = min(water[0], water_list[compare_water_index][0])
                water_width = abs(water[1] - water_list[compare_water_index][1])
                amount.append(water_height * water_width)
        
        return max(amount)

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))