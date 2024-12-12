def product_except_self(nums):
    nums = list(input())
    # nums = [1, 2, 3, 4] 인 경우
    n = len(nums)
    answer = [1] * n
    
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]  
        # 여기까지 했을 때 answer = [1, 1, 2, 6]

    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right  
        right *= nums[i]  
        # 여기까지 하면 answer = [24, 12, 8, 6]
    return answer

'''
# 테스트
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]

print(product_except_self(nums1))  # 출력: [24, 12, 8, 6]
print(product_except_self(nums2))  # 출력: [0, 0, 9, 0, 0]
'''