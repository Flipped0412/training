# 전기버스
# 버스는 0번에서 출발하여 종점인 N번까지 이동
# 한 번 충전으로 최대 이동할 수 있는 정류장 수 K 정해져있음
# 충전기가 설치된 M개의 정류장 번호가 주어질 때
# 최소 몇번의 충전을 해야 종점에 도착할 수 있는지 출력
# 종점에 도착할 수 없는 경우 0

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    cnt = 0
    current = 0
    arr = [0] * (N + 1)
    flag = True

    for i in range(N + 1):
        if i in station:
            arr[i] = 1

    while flag:
        for index in range(K, 0, -1):
            # 종료조건 current 가 N에 도달
            if current + K >= N:
                flag = False
                break
            elif arr[current + index] == 1:
                current += index
                cnt += 1
                break
        else:
            cnt = 0
            flag = False
            break

    print(f"#{tc} {cnt}")