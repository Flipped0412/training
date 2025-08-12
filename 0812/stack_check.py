T = int(input())

for test_case in range(1, T + 1):
    words = input()
    words_list = []

    for word in words:
        words_list.append(word)

    while True:
        for index in range(len(words_list) - 1):
            if words_list[index] == words_list[index + 1]:
                del words_list[index : index + 2]
                break
        else:
            break

    print(f"#{test_case} {len(words_list)}")
