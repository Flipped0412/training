# # r, c에서 시작하는 등산로의 길이를 반환하는 함수
# def solve(r, c):
#     result = 1  # 현재 위치도 등산로의 일부
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     while True:
#         # 상하좌우에 인접한 칸 확인
#         min_r = r
#         min_c = c
#         # 인접한 칸 중에서 제일 작은거 찾기
#         # 단 , 기준점은 현재 위치
#         # 제일 작은 칸이 나보다 작으면, 거기로 이동
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if 0 <= nr < N and 0 <= nc < N:
#                 if arr[nr][nc] < arr[min_r][min_c]:
#                     min_r = nr
#                     min_c = nc
#         # 만약에 arr[r][c] 보다 작은 칸이 있으면 바뀌었을 것
#         # 아니면 min_r, min_c 가 시작점
#         if (r, c) != (min_r, min_c):
#             # 제일 낮은 칸으로 이동
#             r = min_r
#             c = min_c
#             result += 1
#         else:  # 나보다 작은 칸이 없음
#             return result  # 결과 반환
#
#
# # 2차원 배열의 모든 칸에서 등산로 찾기
# # 등산로 찾기 과정
# #   상하좌우 인접한 칸 확인, 나보다 작은 것들 중 제일 작은 칸 찾기
# #   해당 칸으로 이동해서 등산로 찾기 반복
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 2차원 배열 모든 카네서 등산로 찾기
#     max_length = 0
#     for i in range(N):
#         for j in range(N):
#             length = solve(i, j)
#             if length > max_length:
#                 max_length = length
#
#     print(f"#{tc} {max_length}")

def check_path(row, col):
    minus_row = [-1, 1, 0, 0]
    minus_col = [0, 0, 1, -1]

    for i in range(4):
        check_row = row + minus_row[i]
        check_col = col + minus_col[i]
        if arr[row][col] > arr[check_row][check_col]:
            pass


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_root = 0

    for row in range(N):
        for col in range(N):
            path_len = check_path(row, col)
            pass
    pass