# 여행 짐 꾸리기 최적 패킹 프로그램 (0/1 Knapsack)

# 물건 정보
items = [
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4)
]

# 사용자 입력
W = int(input("배낭 용량 입력 : "))

n = len(items)

# DP 테이블 A[i][w] : i번째 물건까지 고려했을 때, 용량 w에서의 최대 만족도
A = [[0] * (W + 1) for _ in range(n + 1)]

# Bottom-up DP
for i in range(1, n + 1):
    name, wt, value = items[i - 1]
    for w in range(1, W + 1):
        if wt > w:
            # 현재 물건을 못 넣는 경우
            A[i][w] = A[i - 1][w]
        else:
            # 넣지 않는 경우 vs 넣는 경우 중 큰 값 선택
            A[i][w] = max(A[i - 1][w], value + A[i - 1][w - wt])

# 최대 만족도
max_value = A[n][W]

# 역추적(Backtracking): 어떤 물건을 선택했는지 확인
selected_items = []
w = W
for i in range(n, 0, -1):
    if A[i][w] != A[i - 1][w]:  # 물건 i가 선택된 경우
        name, wt, value = items[i - 1]
        selected_items.append(name)
        w -= wt  # 무게 줄이기

selected_items.reverse()  # 원래 순서로 정렬

# 결과 출력
print("최대 만족도:", max_value)
print("선택된 물건:", selected_items)
