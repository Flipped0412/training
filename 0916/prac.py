V, E = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(E)]
S, G = map(int, input().split())
flag = 0
map_list = [[]] * (V + 1)

for idx in arr:
    map_list.insert(idx[0], idx[1])

print(map_list)