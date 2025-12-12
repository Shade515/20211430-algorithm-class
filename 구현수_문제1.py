n = int(input("계단 개수 입력 : "))

# n이 1이나 2면 바로 출력하게
if n == 1:
    print(f"{n}개의 계단을 오르는 방법의 수 : 1가지")
elif n == 2:
    print(f"{n}개의 계단을 오르는 방법의 수 : 2가지")
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(f"{n}개의 계단을 오르는 방법의 수는 {dp[n]}가지입니다.")
