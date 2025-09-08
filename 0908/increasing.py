T= int(input())
for tc in range(1, T+1):
    N = int(input())
    num_li = list(map(int, input().split()))
    num_join = ''.join(*num_li)
    current = 0
    max_num = 0
    temp = 0

    for index in range(len(num_join)):
        intNum = int(num_join[index])
        if intNum >= current:
            pass
        else:
            if index == 0:
                pass
            max_num = max(max_num, intNum * int(num_join[index - 1]))
