# 문서 검색
# 메모리 31120KB 시간 36ms

long = input()
short = input()

N = len(long)
M = len(short)

# 결과 개수
count = 0

# 문자열 탐색을 위한 인덱스 초기화
i = 0

# long 문자열을 순회하면서 short 문자열을 찾음
while i <= N - M:
    if long[i:i+M] == short:
        # long의 일부와 short가 일치하면 count를 증가시키고
        # short의 길이만큼 인덱스를 이동하여 중복 방지
        count += 1
        i += M
    else:
        # 일치하지 않으면 인덱스를 하나만 이동
        i += 1

# 결과 출력
print(count)
