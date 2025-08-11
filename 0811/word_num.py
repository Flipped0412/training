T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = {}
    max_char = 0

    for s1_index in range(len(str1)):
        for s2_index in range(len(str2)):
            if str1[s1_index] == str2[s2_index]:
                if str1[s1_index] == str2[s2_index] and result[str1[s1_index]] != 0:
                    result[str1[s1_index]] = 0
                elif str1[s1_index] == str2[s2_index]:
                    result[str1[s1_index]] += 1

    for key in result:
        if result[key] > max_char:
            max_char = result[key]

    print(f"#{test_case} {max_char}")
