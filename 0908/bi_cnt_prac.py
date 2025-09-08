arr = [1, 2, 3, 4]

# i: 0~2^n == i번째 부분집합
for i in range(1 << len(arr)):   # 0 ~ 2^len(arr) - 1 ==> (1 << 4 = 16)
    for idx in range(len(arr)):  # 0 ~ len(arr)-1
        if i & (1 << idx):       # i의 idx번째 비트가 1인지 확인
            print(arr[idx], end=" ")
    print()


arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(len(arr)):
        # 0x1로 표기한 이유? (사실 1, 0b1, 0b0001 등도 다 된다)
        # 하지만 개발자들끼리 약속한 표기법
        if tar & 0x1:
            print(arr[i], end=' ')
        tar >>= 1


for target in range(1 << len(arr)):
    get_sub(target)
    print()
