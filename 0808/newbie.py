T = int(input())

for test_case in range(1, T + 1):
    words = input()
    reverse_words = []
    check = 0

    for word in range(len(words) - 1, -1, -1):
        reverse_words.append(words[word])

    reverse_words = ''.join(reverse_words)

    if words == reverse_words:
        check = 1

    print(f"#{test_case} {check}")
