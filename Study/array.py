class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 결과를 저장할 배열 초기화
        # 왼쪽에서의 누적 곱을 저장할 공간으로 사용
        n = len(nums)
        result = [1] * n

        # 왼쪽에서 오른쪽으로 누적 곱 계산
        # result[i]는 nums[i]를 제외한 왼쪽 부분의 곱
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]  # 현재 값 포함 누적 곱 계산
        
        # 오른쪽에서 왼쪽으로 누적 곱 계산
        # 기존의 result 배열과 곱하여 전체 결과를 구함
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix  # 오른쪽 누적 곱과 현재 값을 곱함
            suffix *= nums[i]  # 현재 값 포함 누적 곱 계산
        
        return result
