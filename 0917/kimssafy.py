# 김싸피와 친구들은 어느 방향으로 이동해야 할까?
# 김싸피와 친구들의 위치가 주어졌을 때, 가장 빨리 선물을 획득하기 위해서는 어느 방향으로 출발 해야 할까?
# 0은 통로, 1은 벽, 2는 선물, 방향 탐색 순서는 시계방향(상우하좌)
# 입력은 첫 줄에 N, M (김싸피와 친구들의 수)
# 이후  M 개의 줄에 김싸피와 친구들의 좌표값
# 5 5
# 2 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 2 1 0 1 0
# 0 0 0 2 0
# 0 3
# 2 4
# 2 2
# 1 1
# 4 1
# # 출력
# 좌
# 하
# 하
# 상
# 우


def bfs(man):
    visited = [[0]*N for _ in range(N)]
    queue = []
    parents_li = []
    queue.append(man)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # 여기서 부터 동작 하겠다.
    # 무슨동작?
    # ==>> 상 우 하 좌 탐색
    while queue: # 첫번째 시행에는 최초 위치만 들어가 있다. 그다음 부터는? > 인접 노드(조건: 갈 수 있는 곳)
        # 다음 행선지 가져오기 >> Q[0]
        # Q[0]이 무엇인지 확인해야해??
        y, x = queue.pop(0) # 최초 시행에 >> 0 3

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            # ny, nx 가 범위 내에 있는지 ex) 0<= nx < N
            # 그게 방문 했던 곳인지
            # 그게 벽인지 아닌ㄴ지
            # 그게 2인지 아닌지 확인
            # 그리고 queue 에 넣기
        pass


N, M = int(input())
present_map = [list(map(int, input().split())) for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(M)]

# 사람 리스트 만들어서 한명씩 뽑아오자
for man in arr:
    bfs(man)
