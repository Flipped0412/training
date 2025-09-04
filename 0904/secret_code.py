hex_to_bin = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111",
}

bit_to_num = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    # 16진수 숫자를 2진수로 변경
    bin_data = []

    for row in data:
        bin_row = ''
        for hex in row:
            bin_row += hex_to_bin[hex]
        bin_data.append(bin_row)

    # 행 우선 순회 하면서, 암호코드 시작점 찾기, 단 행에서 검색은 뒤에서 부터
    result = 0
    for i in range(N):
        j = M*4-1
        while j > 55:
        # for j in range(M * 4 - 1, -1, -1):
            # 코드는 여러줄인데 한 번만 처리되어야 한다.
            # 시작줄에서 처리한다. >>>> 윗 칸이 0인 줄
            if bin_data[i][j] == '1' and bin_data[i-1][j] == '0':  # 암호 코드의 시작점을 찾음!  //// 왜 여긴 문자열
                code = []
                # 숫자 8개 읽기
                # 배율 알아내기 위해서 숫자 하나 읽고 나머지 읽ㄱ
                n1, n2, n3, n4 = 0, 0, 0, 0
                while bin_data[i][j] == "1":  # 여긴 숫자열?
                    n4 += 1
                    j -= 1
                while bin_data[i][j] == "0":
                    n3 += 1
                    j -= 1
                while bin_data[i][j] == '1':
                    n2 += 1
                    j -= 1
                while bin_data[i][j] == '0':
                    n1 += 1
                    j -= 1
                rate = (n1 + n2 + n3 + n4) // 7
                n1 //= rate
                n2 //= rate
                n3 //= rate
                n4 //= rate
                code.append(bit_to_num[(n1, n2, n3, n4)])
                # 나머지 7개 읽기
                for _ in range(7):
                    n1, n2, n3, n4 = 0, 0, 0, 0
                    while bin_data[i][j] == '1':
                        n4 += 1
                        j -= 1
                    while bin_data[i][j] == '0':
                        n3 += 1
                        j -= 1
                    while bin_data[i][j] == '1':
                        n2 += 1
                        j -= 1
                    # 마지막 0은 개수 세지 않고 계산
                    n1 = rate * 7 - n2 - n3 - n4
                    j -= n1
                    n1 //= rate
                    n2 //= rate
                    n3 //= rate
                    n4 //= rate
                    # 숫자 추가
                    code.append(bit_to_num[(n1, n2, n3, n4)])
                # 숫자 8개 구했으니 정상 암호코드인지 확인
                odd_num = code[1] + code[3] + code[5] + code[7]
                even_num = code[0] + code[2] + code[4] + code[6]
                if (odd_num * 3 + even_num) % 10 == 0:
                    # 정상 암호코드, 코드 더하기
                    result += (odd_num + even_num)

            else:
                j -= 1

    print(f"#{tc} {result}")