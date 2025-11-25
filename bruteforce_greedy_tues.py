#========================
# 2. 0/1 배낭 채우기 문제
#========================

def knapsack01_bf(wgt, val, W):
    """브루트포스 방식으로 0/1 Knapsack 문제 해결"""
    # wgt : 물건 무게 리스트, val: 무건 가치 리스트
    # W: 베닝 최대 무게

    n = len(wgt) # 물건의 개수
    bestVal = 0 # 최대가치 초기화

    bestSet = [] # 최적 조합 기록
    count = 0 # 부분집합(조합) 번호 표시용

    for i in range(2 ** n): # 0 ~ 2^n - 1 모든 부분집합 조합 탐색
        count += 1

        # 1. 각 조합에 대해 2진수 비트 패턴 생성=> 리스트에 역순으로 저장
        s = [0] * n # 비트 스트링 초기화
        temp = i
        for j in range(n) : 
            s[j] = temp % 2 # J번째 비트 구하기
            temp = temp // 2 # 다음 비트 이동

        print(f"{i} : 조합의 비트 패턴(선택 여부): {s}")

        # 2. 현재 조합 {i} 의 무게/가치 계산
        semWgt = 0 # 현재 조합{i}의 무게 합
        sumVal = 0 # 현재 조합 {i}의 가치 합
        chosen_items = [] # 선택된 물건 인덱스 저장

        for j in range(n) :
            if s[j] == 1: # j번째 비트가 1이면 즉. j번째 물건을 선택한 경우
            sumWgt += wgt[j]
            sumVal += val[j]
            chosen_items.append(j) # 선택된 j번째 물건 인덱스 포함
        print ("선택된 물건 인덱스:", chosen_items, " / 총 무게 =", sumWgt, " / 총 가치 =", sumVal)

        # 3. 배낭 무게 조건 만족하면 최대값 갱신
        if sumWgt <= W:
            print("배냥 용량 충족")
            if sumVal > bestVal:
                bestVal = sumVal # 최대 가치 갱신
                bestSet = chosen_items[:] # 최저 조합 갱신
                print(" -> 가치 최대값 갱신! 현재 최대 =", bestVal)
            else:
                print(" -> 가치 최대값 갱신 없음.")
        else:
            print(" -> 배낭 용량 초과! 제외")
        
        print()
    return bestVal, bestSet
# 테스트
weight = [10, 20, 30, 25, 35]
value = [60, 100, 120, 70, 85]
bestVal, bestSet = knapsack01_bf(weight, value, 80)
print("최대 가치:", bestVal, "선택된 물건 인덱스", bestSet)
print("="*100)

#===========================================
# 알고리즘 설계 전략 : 탐욕적기법(greedy algoritm)
#===========================================
# 1. 1. 거스름돈 동전 최소화 문제
def coin_change_greedy(coins, amount):
    # 탐욕기법 정의 : 큰 단위부터 사용하기 위해 정렬 - 액면가가 높은 것부터 내림차순 정렬
    coins.sort(reverse = True) # O(nlog n)
    result = [] # (동전 단위, 사용 갯수) 저장
    total_count = 0 # 총 동전 개수
    remain = amount # 남은 금액

    for coin in coins:
        cnt = remain // coin
        result.append((coin, cnt))
        total_count += cnt
        remain -= coin * cnt # 남은 금액 갱신

    if remain == 0:
        return total_count, result # 사용된 동전 개수와 조합 반환
    else:
        return -1, [] # 정확히 만들 수 없는 경우

# 테스트
# coins


#==========================
# 2. 분할가능한(Factional) 배낭문제
# 정렬 + 배낭 채우기 문제
def kanpsackFrac_greedy(weights, values, W) :
    # 반환 : (최대가치, 가방에 채운 물건 기록)
    # items : (비율, 무게, 가치, 인덱스)

    n = len(weights) # 물건의 개수

    # --- 단계 1: 단위 무게당 가격 비율 ratio 생성 : O(n)---
    items = []
    for i in range(n):
        items.append((values[i]/weights[i], weights[i]. values[i], i))

    # --- 단계 2: 단위 무게당 가격의 내림차순 정렬 : O(n logn) --- 탐욕적
    items.sort(reverse = True, key = lambda x : x[0])

    # --- 단계 3: Greedy 채우기 : O(n)---
    bestVal = 0
    bag_with_items = [] # 가방에 채워지는 물건 기록

    for ratio, wgt, val, idx in items:  #비율이 높은 순서부터 물건 채워넣기
        if W <= 0 : # 배낭이 꽉 채워진 경우
            break
        if W >= wgt: # 물건을 통채로 넣을 수 있는 경우
            W -= wgt    # 넣은 후 남은 용량 갱신
            bestVal += value# 최대 가치 증가
            bag_with_items.append(("full",idx, wgt, val)) # 물건을 통채로 넣음
        else: # W < wgt 즉, 물건의 일부만 넣어야하는 경우
            fraction = W / wgt
            bestVal += val * fraction
            bag_with_items.append(("part",idx, W, val*fraction)) # 물건 일부 넣음
            W = 0 # 가방이 꽉 찬 상태
            break

    return bestVal, bag_with_items

#test
weights = [12, 10, 8]
values = [120, 80, 60]
W = 18
bestVal, item = kanpsackFrac_greedy(weights, values, W)
print(f"테스트 데이터 : 최대 가치 = {bestVal}")