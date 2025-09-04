A = list(range(1, 13))
N = int(input())
res = []

def dfs(idx, picked):
    if len(picked) == N:
        res.append(tuple(picked))
        return