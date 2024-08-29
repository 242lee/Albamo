# 1543번 백준 문서검색

## 문제

영어로만 이루어진 어떤 문서를 검색하는 함수를 만들려고 함
이 함수는 어떤 단어가 총 몇번 등장하는지 셈
중복되지 않게 해야함

검색하려는 단어가 최대 몇 번 중복되지않게 등장하는지 구하라

첫째 줄에 문서가 주어진다. 문서의 길이는 최대 2500이다. 둘째 줄에 검색하고 싶은 단어가 주어진다.
이 길이는 최대 50이다. 문서와 단어는 알파벳 소문자와 공백으로 이루어져 있다.


### 오답 코드

```python
from itertools import groupby

# 입력값을 공백이 있는것과 없는것을 기준으로 받는 함수
def findblank(doc):
    # 공백이 있는 경우
    if ' ' in doc:
        return doc.split()
    # 공백이 없는 경우 연속된 문자 그룹화
    else:
        return [''.join(group) for _, group in groupby(doc)]

doc = input()
word = input()
doc_list = findblank(doc)
word_list = findblank(word)
length_difference = len(doc_list) - len(word_list)
result = 0
visited = [0] * len(doc_list)

for i in range(0, length_difference + 1):
    cnt = 0
    for j in range(len(word_list)):
        if doc_list[i+j] == word_list[j] and visited[i+j] == 0:
            cnt += 1
        else:
            break

    if cnt == len(word_list):
        result += 1
        for j in range(len(word_list)):
            visited[i+j] = 1

print(result)
```

> 테스트케이스는 다 맞았지만 제출했을 때 틀림
-  시간초과 때문이라 생각함 나는. gpt도 이유를 모름

### 정답 코드

```python
doc = input().strip()
word = input().strip()

doc_len = len(doc)
word_len = len(word)

count = 0
i = 0

while i <= doc_len - word_len:
    if doc[i:i + word_len] == word:
        count += 1
        i += word_len   # 단어 길이만큼 건너뛰기
    else:
        i += 1  # 다르면 다음 글자로 이동

print(count)
```

> while문으로 풀어서 해볼까 해서 해봤지만 이건 됐다..

- visited 리스트 없이도 단어가 중복되지 않게 세어짐
- 시간 복잡도는 O(N)으로, 매우 효율적입니다.


### 다른 사람의 미친 정답코드

이 코드는 매우 간결하고 효율적으로 문제를 해결합니다. 아래에서 이 코드가 왜 정답인지 설명드리겠습니다.

### 코드 분석

```python
a = input()
b = input()

a = a.split(b)
print(len(a) - 1)
```

### 코드 설명

1. **`input()`으로 문서와 단어를 입력받음**:
   - `a`는 문서 전체를, `b`는 찾고자 하는 단어를 입력받습니다.

2. **`split(b)` 사용**:
   - `a.split(b)`는 문자열 `a`를 문자열 `b`를 기준으로 나눕니다. 즉, 문서에서 `b`가 등장하는 모든 부분을 기준으로 문서를 분리합니다.
   - 예를 들어, 문서가 `"ababababa"`이고 단어가 `"aba"`라면, `a.split(b)`는 `['', 'b', 'b', '']`와 같이 나뉘게 됩니다.

3. **`len(a) - 1`**:
   - `split()` 함수는 `b`를 기준으로 나누기 때문에, `b`가 등장한 횟수만큼 리스트의 요소가 생성됩니다.
   - `len(a)`는 분리된 요소들의 수를 반환하며, 여기에서 `-1`을 하면 `b`가 몇 번 등장했는지를 알 수 있습니다.

### 코드가 정답인 이유

- **효율성**: 이 코드는 단순히 문서를 한 번 순회하며, 단어가 몇 번 등장하는지를 빠르게 계산합니다. 시간 복잡도는 O(N)이며, N은 문서의 길이입니다.
- **정확성**: `split()` 메서드는 정확하게 문자열 `b`가 등장하는 모든 위치를 찾아내고, 이를 기준으로 분리합니다. 따라서 단어 `b`가 중복되지 않게 최대 몇 번 등장하는지를 정확하게 계산할 수 있습니다.
- **간결성**: 코드가 매우 간결하고, `split()` 메서드를 사용하여 직접적으로 문제를 해결합니다. 복잡한 로직 없이도 문제의 핵심을 잘 처리합니다.

### 예시

```python
a = "ababababa"
b = "aba"

# a.split(b) 결과: ['', 'b', 'b', '']
# len(a.split(b)) = 4
# 정답: 4 - 1 = 3
```

### 결론

이 코드는 단어 `b`가 문서 `a`에서 중복되지 않게 몇 번 등장하는지를 매우 효율적으로 계산합니다. `split()` 메서드를 사용하여 정확하고 간결하게 문제를 해결할 수 있기 때문에, 이 코드는 정답으로 처리됩니다.