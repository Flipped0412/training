T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]
    result = []

    for index in range(N):
        reverse_words_row = []
        reverse_words_col = []
        row_words = []
        col_words = []

        for word in range(N - 1, N - M - 1, -1):  # 역
            reverse_words_row.append(words[index][word])
            reverse_words_col.append(words[word][index])

        for word in range(N - M, N):  # 정
            row_words.append(words[index][word])
            col_words.append(words[word][index])

        reverse_words_row = ''.join(reverse_words_row)
        reverse_words_col = ''.join(reverse_words_col)
        row_words = ''.join(row_words)
        col_words = ''.join(col_words)

        if row_words == reverse_words_row:
            result = reverse_words_row
        elif col_words == reverse_words_col:
            result = reverse_words_col

    print(f"#{test_case} {result}")
