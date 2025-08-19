# 요소가 N개인 수열의 모든 순서 구하기
# 123 : 1,2,3 / 1,3,2 / 2,1,3 / 2,3,1 / 3,1,2 / 3,2,1

arr = [1,2,3]
N = len(arr)
perm_arr = [-1] * N
check = [0] * N

# perm_arr의 k번 인덱스 각 요소 넣어보기
def perm(k):
    if k == N:
        print(perm_arr)
        return

    for i in range(N):
        if check[i] == 0:
            perm_arr[k] = arr[i]
            check[i] = 1
            perm(k+1)
            check[i] = 0

perm(0)

###### 그림 그려보기 ######