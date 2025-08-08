T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    check_dic = {}
    max_val = 0

    for word in str1:
        check_dic[word] = 0
        
    for word in str2:
        if word in str1:
            check_dic[word] += 1

    for key in check_dic:
        if check_dic[key] > max_val:
            max_val = check_dic[key]

    print(f"#{test_case} {max_val}")