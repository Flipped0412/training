import sys, heapq
sys.stdin = open('input_cow.txt')  # 필요하면 사용

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    L = [0] * (N + 1)
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        Li, Di = map(int, input().split())
        L[i], D[i] = Li, Di
    attacks = [int(input()) for _ in range(M)]

    # 상태
    broken = set()        # 현재 고장난 외양간
    pq = []               # 후보: (-L/D, -L, i)  ← 최대힙 흉내
    busy_barn = None      # 지금 수리 중인 외양간 (없으면 None)
    busy_until = 0        # '아침' 완료일(= 시작일 + D)
    cur_loss = 0          # 현재 손실 합
    ans = 0               # 총 손실

    for day in range(1, M + 1):
        # 1) 아침: 수리 완료 처리
        if busy_barn is not None and day == busy_until:
            b = busy_barn
            if b in broken:
                broken.remove(b)
                cur_loss -= L[b]
            busy_barn = None

        # 2) 아침: 비었으면 새 수리 착수 (우선순위: L/D 큰 순, 동률은 L 큰 순)
        if busy_barn is None:
            # 힙 top이 이미 고장 아님(=수리 완료된 뒤 남은 찌꺼기)일 수 있으니 정리
            while pq and pq[0][2] not in broken:
                heapq.heappop(pq)
            if pq:
                _, _, b = heapq.heappop(pq)
                busy_barn = b
                busy_until = day + D[b]  # D일 뒤 '아침' 완료

        # 3) 밤: 공격 반영
        a = attacks[day - 1]
        if a not in broken:
            broken.add(a)
            cur_loss += L[a]
            # 부동소수점으로도 충분(문제 크기 작음). 정수키 쓰고 싶으면 L[a]*10000//D[a]
            heapq.heappush(pq, (-(L[a] / D[a]), -L[a], a))

        # 4) 그날 손실 누적
        ans += cur_loss

    print(f"#{tc} {ans}")
