# def select(arr, k):
#     for i in range(0, k - 1):
#         min_index = i
#         for j in range(i + 1, k):
#             if arr[min_index] > arr[j]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# n = 10
# li = [67, 39, 16, 49, 60, 28, 8, 85, 89, 11]

# print(select(li, n))

# tc = int(input())
# ladder = [list(map(int, input().split())) for _ in range(100)]
# # print(ladder)

# for row in range(100):
#     print(row, '열 진행 중!')
#     if ladder[row][0] == 1:
#         temp_row = row
#         start_row = row
#         check = True
#         while check:
#             for col in range(99):
#                 print(temp_row, col, '이동 중!')
#                 if ladder[row + 1][col] == 1:  # 우 확인되면
#                     for move_row in range(100):
#                         if ladder[row + move_row][col] == 0:
#                             temp_row = row + move_row
#                             break
#                 elif ladder[row -1 ][col] == 1:  # 좌 확인되면
#                     for move_row in range(100):
#                         if ladder[row - move_row][col] == 0:
#                             temp_row = row - move_row
#                             break
#                 if ladder[row][col + 1] == 2:
#                     result = start_row
#                     check = False
#                     break
#                 elif col == 98:
#                     check = False
                
# print(f"#{tc} {result}")


# 10개의 테스트 케이스를 처리한다고 가정
for t in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    result = 0

    # 1. 0번 행의 모든 열(x좌표)을 시작점으로 하여 하나씩 테스트
    for start_x in range(100):
        # 현재 시작점이 사다리의 일부가 아니면 건너뜀
        if ladder[0][start_x] == 0:
            continue

        # 2. 현재 위치(current_x, current_y)를 설정하고 아래로 탐색 시작
        current_x = start_x
        current_y = 0

        # 아래쪽 끝(99번 행)에 도달할 때까지 이동
        while current_y < 99:
            # 3. 좌/우를 먼저 살핀다
            # 왼쪽으로 길이 있고, 방문하지 않았다면
            # (이동 방향은 아래로만 가므로 방문 여부 체크는 불필요)
            if current_x > 0 and ladder[current_y][current_x - 1] == 1:
                # 길이 끊길 때까지 왼쪽으로 계속 이동
                while current_x > 0 and ladder[current_y][current_x - 1] == 1:
                    current_x -= 1
            
            # 오른쪽으로 길이 있다면
            elif current_x < 99 and ladder[current_y][current_x + 1] == 1:
                # 길이 끊길 때까지 오른쪽으로 계속 이동
                while current_x < 99 and ladder[current_y][current_x + 1] == 1:
                    current_x += 1
            
            # 4. 좌/우 이동을 마친 후 아래로 한 칸 이동
            current_y += 1
        
        # 5. 맨 아래까지 도착했을 때, 그 위치가 '2'인지 확인
        if ladder[current_y][current_x] == 2:
            result = start_x  # 도착했다면, 해당 시작점(start_x)이 정답
            break  # 정답을 찾았으므로 더 이상 다른 시작점을 탐색할 필요 없음

    print(f"#{tc} {result}")