# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

V = 7  # 최대 정점 정보
E = 8

adj = [[0]*(v+1) for _ in range(V+1)]  # 각 정점간 연결 정보
edges = list(map(int, input().split()))   # edges 두 개씩 읽으면서 adj에 표시하기

for i in range(0, E*2, 2):
    pass