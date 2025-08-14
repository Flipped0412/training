# maze = [
#     [1, 1, 1, 0, 0],
#     [0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 1, 0, 2],
#     [0, 1, 1, 1, 1]
# ]
#

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = len(maze)
    sr, sc = 0, 0


    stack = [(sr, sc)]
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while stack:
        cr, cc = stack[-1]

        if maze[cr][cc] == 2:
            print(stack)
            break

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break

        else:
            stack.pop()

    else:
        print(-1)
