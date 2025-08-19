T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    portals = list(map(int, input().split()))
    result = 0

    for i in range(2, N):  # 인덱스 번호를 1부터 시작하기 위해 1씩 증가시켰으며, 처음과 마지막 인덱스는 확인하지 않아도 됨으로 제외
        result += i - portals[i - 1] + 1

    result += N - 1  # 모든 방을 1회는 지나옴으로 추가해준다

    print(f"#{test_case} {result}")
