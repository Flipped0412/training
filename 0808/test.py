# words = input()
# reverse_words = []
#
# for word in range(len(words)-1, -1, -1):
#     reverse_words.append(words[word])
#
# print(''.join(reverse_words))


# N, M = map(int, input().split())
# words = [input() for _ in range(N)]
# print(words, type(words))
#
# result = []
#
# for index in range(N):
#     reverse_words_row = []
#     reverse_words_col = []
#     for word in range(M - 1, -1, -1):
#         print(word, 'word 는 인덱스')
#         reverse_words_row.append(words[index][word])
#         print(words[index][word], '가로 더하기 단어들')
#         reverse_words_col.append(words[word][index])
#         print(words[word][index], ' 세로 더하기 단어들')
#
#     print(reverse_words_row, '가로 더한 결과')
#     print(reverse_words_col, '세로 더한 결과')
#
#     reverse_words_row = ''.join(reverse_words_row)
#     reverse_words_col = ''.join(reverse_words_col)
#
#     if words[index] == reverse_words_row:
#         result = reverse_words_row
#     elif words[index] == reverse_words_col:
#         result = reverse_words_col
#
# print(f"#{1} {result}")

N, M = map(int, input().split())
words = [input() for _ in range(N)]
# print(words, type(words))

result = []

for index in range(N):
    reverse_words_row = []
    reverse_words_col = []
    col_words = []

    for word in range(M - 1, -1, -1):
        reverse_words_row.append(words[index][word])
        reverse_words_col.append(words[word][index])

    for word in range(M):
        col_words.append(words[word][index])

    reverse_words_row = ''.join(reverse_words_row)
    reverse_words_col = ''.join(reverse_words_col)
    col_words = ''.join(col_words)

    print(reverse_words_row, '가로 역 더한 결과')
    print(reverse_words_col, '세로 역 더한 결과')
    print(col_words, '세로 정 방향')

    if words[index] == reverse_words_row:
        result = reverse_words_row
    elif col_words == reverse_words_col:
        result = reverse_words_col

print(f"#{1} {result}")