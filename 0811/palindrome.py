# 회문
# 8*8 평면 글자판에 제시된 길이를 가진 회문의 개수를 구하라

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    cnt = 0
    temp = [''] * N

    # 가로 회문 확인
    for row in range(8):
        for col in range(8 - N + 1):
            for idx in range(N):
                temp[idx] = arr[row][col + idx]

            origin = temp.copy()
            temp.reverse()

            if temp == origin and temp[0] != '':
                cnt += 1

    # 세로 회문 확인
    for row in range(8 - N + 1):
        for col in range(8):
            for idx in range(N):
                temp[idx] = arr[row + idx][col]

            origin = temp.copy()
            temp.reverse()

            if temp == origin:
                cnt += 1

    print(f"#{tc} {cnt}")