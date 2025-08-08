def selection_sort(a, N):
        for i in range(N - 1):
            min_idx = i
            for j in range(i + 1, N):
                if check_dic[a[min_idx]] > check_dic[a[j]]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
        return a

T = int(input())

for test_case in range(1, T + 1):
    test_case, N = input().split()
    test_words = list(input().split())

    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    check_dic = {}
    n = 0
        
    for word in num_list:
        check_dic[word] = n
        n += 1

    # print(check_dic)

    sort_words = selection_sort(test_words, len(test_words))
    # print(test_case)
    print(test_case, ' '.join(sort_words))