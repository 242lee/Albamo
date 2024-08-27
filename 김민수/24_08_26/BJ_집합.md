# 백준 집합

## 문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

### 코드
```python
M = int(input())
S = []
for _ in range(M):
    plus = input().split()
    if plus[0] == 'add':
        if S:   # 비어있으면
            S.append(plus[1])
        else:
            pass

    elif plus[0] == 'remove':
        if S:
            S.pop(0)
        else:
            pass

    elif plus[0] == 'check':
        if S:
            print(1)
        else:
            print(0)

    elif plus[0] == 'toggle':
        if S:
            S.pop(0)
        else:
            S.append(plus[1])

    elif plus[0] == 'all':
        for i in range(1, 21):
            S.append(i)

    elif plus[0] == 'empty':
        S.clear()
```

> 메모리 초과 or 시간초과 -> 로직과 입력 받는 값 변경

### 정답 코드

```python
import sys

input = sys.stdin.readline  # 빠른 입력 처리를 위해 sys.stdin.readline 사용

# 집합을 관리할 리스트: index 1부터 20까지 사용 (0번 인덱스는 사용하지 않음)
is_present = [0] * 21

num_operations = int(input())  # 명령어의 수
for _ in range(num_operations):
    operation = input().strip()  # 입력의 끝에 있는 공백 제거
    
    # 명령어 처리
    if operation[:3] == 'all':
        is_present = [1] * 21  # 모든 숫자를 포함하도록 리스트 설정
    elif operation[:3] == 'emp':
        is_present = [0] * 21  # 모든 숫자를 비우도록 리스트 초기화
    else:
        command, value = operation.split()
        value = int(value)
        
        if command == 'add' and not is_present[value]:
            is_present[value] = 1  # 리스트에서 해당 숫자를 추가
        elif command == 'remove' and is_present[value]:
            is_present[value] = 0  # 리스트에서 해당 숫자를 제거
        elif command == 'toggle':
            is_present[value] = 0 if is_present[value] else 1  # 리스트에서 해당 숫자를 토글
        elif command == 'check':
            print('1' if is_present[value] else '0')  # 리스트에 해당 숫자가 있는지 확인

```

## 주요 차이점

### 주요 차이점:

1. **데이터 구조 사용 방식**:
   - **제공된 코드**: `is_present`는 리스트로 사용되며, 리스트의 원소로 `value` 값을 추가하고 제거하는 방식으로 구현되어 있습니다. 이 리스트는 특정 명령어에 따라 원소를 추가하거나 제거합니다.
   - **최적화된 코드**: `is_present`는 고정된 크기의 리스트 `[0] * 21`로, 1부터 20까지의 숫자에 대해 포함 여부를 비트마스크처럼 관리합니다. 각 숫자의 포함 여부를 0 또는 1로 표시하여 메모리와 성능을 최적화했습니다.

2. **명령어 처리**:
   - **제공된 코드**: `add`, `remove`, `check`, `toggle` 등의 명령어가 각기 다른 방식으로 구현되어 있으며, 리스트가 비어있는지 확인한 후 동작을 수행합니다. 특히, `add`와 `toggle` 명령어에서 `is_present`가 비어있으면 아무 작업도 수행하지 않습니다.
   - **최적화된 코드**: 명령어들은 `is_present` 리스트의 특정 인덱스를 직접 조작하는 방식으로 동작합니다. 예를 들어, `add`는 `is_present[value] = 1`로, `remove`는 `is_present[value] = 0`으로 처리합니다. 이 방식은 명령어 처리 속도를 높이고 불필요한 조건문을 제거하여 간결하고 효율적입니다.

3. **특정 명령어 구현**:
   - **제공된 코드**: `all` 명령어는 1부터 20까지의 숫자를 리스트에 추가하는 방식으로 구현되었습니다. `empty` 명령어는 리스트를 비우는 `clear()` 메서드를 사용합니다.
   - **최적화된 코드**: `all` 명령어는 `is_present = [1] * 21`로 모든 숫자를 한 번에 포함시키며, `empty` 명령어는 `is_present = [0] * 21`로 리스트를 초기화합니다. 이 방식은 메모리를 효율적으로 사용하며, 명령어 수행 속도를 높입니다.

4. **입력 처리**:
   - **제공된 코드**: `input()` 함수를 사용해 명령어를 읽습니다. 각 명령어는 `split()`으로 나눠져 처리됩니다.
   - **최적화된 코드**: `sys.stdin.readline()`을 사용해 입력을 읽고, 빠르게 명령어를 처리합니다. 이 방식은 많은 양의 입력을 처리할 때 더 효율적입니다.

    
### 요약:
- **메모리 관리**: 최적화된 코드는 메모리를 고정 크기의 리스트로 효율적으로 사용합니다.
- **명령어 처리 속도**: 명령어에 따른 조건문과 연산이 간소화되어 있으며, 직접 리스트 인덱스를 조작함으로써 속도가 향상됩니다.
- **입력 처리 방식**: 최적화된 코드는 `sys.stdin.readline()`을 사용해 많은 양의 입력을 효율적으로 처리합니다.

이러한 차이점들이 코드의 성능과 메모리 효율성을 높이는 데 기여하고 있습니다. 코드의 구조를 최적화한 것이 차이를 만든 핵심입니다.