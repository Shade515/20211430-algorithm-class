#알고리즘 설계 전략 : 분할과 정복(Divide & Conquer)
#======================================================
# 1. k번째 작은 수를 찾는 문제 (k-th smallest element)
# 1. 분할 함수 정의 - 퀵 정렬의 분할 함수 사용
def partition(A, left, right):
    pivot = A[left] # pivot 설정
    i = left + 1    # 왼쪽 서브리스트 포인터
    j = right       # 오른쪽 서브리스트 포인터

    while True:
        while i <= j and A[j] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i > j :
            break

        A[i], A[j] = A[j], A[i]

    A[left], A[j] = A[j], A[left]
    return j

# (1) 억지기법 : 정렬 이용, 시간복잡도는 0(n log n)
def kth_smallest_bf(arr, k):
    B = sorted(arr) # 0(n log n)
    return B[k-1] # k번째 작은 수의 인덱스 사용

# (2) 축소정복 전략 사용 = 재귀함수와 분할함수 이용
# 시간복잡도 : 평균 O(n), 최악 O(n^2)
def quick_select(A, left, right, k):
    if left == right : # 함수 호출 종료
        return A[left]

    # 피봇을 배열 A의 첫번째 요소롤 설정
    pos = partition(A, left, right)
    # pos는 0부터 시작하는 인덱스 -> 순서로 변환시 pos + 1
    # k와 pos +1을 비교
    if k + left == pos + 1 : # case 1 - 피벗이 k번째인 경우
        return A[pos]
    elif k + left < pos + 1 : # case 2 - k번째 작은수가 피벗의 왼쪽에 나타나는 경우
        quick_select(A, left, pos - 1, k)
    else:
        # case 3 - k번째 작은수가 피벗의 오른쪽에 나타나는 경우 k를 갱신
        quick_select(A, pos + 1, right, k - (pos + 1 - left))

#테스트
A1 = [7,2,1,8,6,3,5,4,0]
A2 = A1.copy()
k = 3
print("억지기법 : ", kth_smallest_bf(A1, k))
print("축소정복 : ", quick_select(A2, 0, len(A2)-1, k))
print("="*100)

#================================================
# 2. MergeSort 병합정렬
# 오름차순으로 정렬, 중복된 데이터 허용, 안정적 정렬, 추가 메모리 사용!
# 1. 병합 함수
def merge(A, left, mid, right):
    # 1. 임시 리스트 생성 : 크기 = right = left + 1
    sorted_list = [0] * (right - left + 1)

    # 2. 두 부분 리스트의 시작 인덱스
    i = left    # 왼쪽 부분리스트 시작 index
    j = mid + 1 # 오른쪽 부분 리스트의 시작 index
    k = 0       # 임시 리스트의 시작 index
    # 3. 두 정렬 리스트를 비교하여 임시리스트에 기록
    while i <= mid and j <= right : #O(n)
        if A[i] <= A[j]
            sorted_list[k] = A[i]
            i += 1
            k += 1
    # 4. 왼쪽 부분 리스트가 남아있는경우 모두 복사
    while i <= mid :
        sorted_list[k] = A[i]
        i += 1
        k += 1
    # 4. 오른쪽 부분 리스트가 남아있는경우 모두 복사

    # 5. 임시리스트의 결과를 원래 리스트 A에 덮어쓰기
    for t in range(k):
        A[left + t ] = sorted_list[t]

# 병합 정렬 함수
def merge_sort(A, left, right):
    if left < right :   # 항목이 두개 이상인 경우에만 분할 = O(log n)
        mid = (left + right) // 2
        # 왼쪽 부분 정렬
        merge_sort(A, left, mid)
        # 오른쪽 부분 정렬
        merge_sort(A, mid + 1, right)
        # 정렬된 두 부분 리스트를 병합 = O(n)
        merge(A, left, mid, right)

# 테스트
A = [38,27,43,3,9,82,10]
print("정렬 전:", A)
merge_sort(A, 0, len(A) - 1)
print("정렬 후 :", A)
print()

# 프로그래밍문제 1 : 병합정렬 기반 중복제거 알고리즘

#===========================
# 알고리즘 설계 전략 : 동적계획법 (Dynamic Programming)
#==================================
# 1. fibonacci sequence (피보나치 수열) 문제
# (1) 동적계획법 - 메모제이션 방식 - top-down 방식 - 주어진 문제에서 작은 문제로 해결하는 방식

# 1. 전역 변수로 메모이제이션 배열 준비 (0~10까지)
mom = [None] * 11

def fib_dp_mem(n): # fib(n) =?
    if mem[n] is None:
        if n< 2:    # 처음 계산하는 값이면 기록
            mem[n] = n  #fib(0) = 0. fib(1) = 1
        else:       # 중복 계산 피함
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

# 테스트
print("n = 6 => fib(6) : ", fib_dp_mem(6))
print("mem = ", mem[:7]) # 결과 수열 출력
print("="*100)

# (2) 동적계획법 - 테이블화 방식 - bottom-up 방식 - 작은 문제부터 큰 문제로 주어진 문제를 해결 방식
# DP 테이블 생성 - 지역변수 처리, 반복문
# 시간복잡도 : O(n)
def fis_dp_tab(n):
    # 1. 1차원 리스트 준비
    table = [None] * (n + 1)
    table[0] = 0 
    table[1] = 1

    # 2. 상향식으로 테이블 채우기
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table

# 테스트
table = fib_dp_tab(6)
print(table[6])
print("table = ", table[:7])


## 빠진게 좀 많은거같은디

