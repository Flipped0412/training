# 갈 수 있는데 까지 가보고 충전소 없으면
# 되돌아 오면서 가장 먼저 만나는 충전소에서 충전하기
T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    charges = list(map(int,input().split()))
    stations = [0] * (N+1) # 충전기가 있으면 1, 없으면 0
    for num in charges: #충전기가 있는 정류장 표시
        stations[num] = 1
 
    # 현재 위치 기준으로 제일 멀리 갈 수 있는 곳 부터 되돌아 오면서 탐색
    # 목적지에 도착할 때 까지 탐색....while
    current = 0 #시작점이 0이니까..
    cnt = 0 # 충전 횟수
    while current + K < N:
        # 어디에서 충전해야 하는지 찾는 반복문
        # 더 이상 충전 할 필요가 없으면 멈추기 
        # if current + K >= N:   # N이 목적지 번호
        #     break   #
        # 현재 위치에서 갈 수 있는 제일 먼 곳 부터, 충전소 찾기
        # 제일 먼곳 : current + K, step = -1
        is_find = False
        for i in range(current+K, current,-1): # i: 충전소 확인하려는 정류장 번호
            if stations[i] == 1:
                current = i # i번에서 충전
                cnt += 1 # 충전 횟수도 증가
                is_find = True
                break   # 충전소 찾았다 멈춰
        if not is_find: #충전소를 못찾았다면?
            cnt = 0
            break # 다음정류장 못가니까 멈춰
    print(f'#{tc} {cnt}')

    ##### import sys; sys.stdin = open('test_input.txt') ##### 입력값 바로 넣기