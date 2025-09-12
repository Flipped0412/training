N = int(input())
arr = [list(map(str, input())) for _ in range(8)]
cnt = 0
temp = ['']*N

# 가로 회문 확인
for row in range(8):
    for col in range(8 - N + 1):
        for idx in range(N):
            temp[idx] = arr[row][col + idx]

        print(temp)
        origin = temp.copy()
        temp.reverse()

        if temp == origin and temp[0] != '':
            cnt += 1

# 세로 회문 확인
for row in range(8 - N + 1):
    for col in range(8):
        for idx in range(N):
            temp[idx] = arr[row + idx][col]

        print(temp)
        origin = temp.copy()
        temp.reverse()

        if temp == origin:
            cnt += 1

print(f"#{1} {cnt}")
#
# a = [1, 2, 3, 4]
# a.reverse()
# print(a)