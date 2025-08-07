# boxes = list(map(int, input().split()))

# boxes = sorted(boxes)
# print(boxes)
# print(boxes[-1], boxes[0])

# dump_count = int(input())
# boxes = list(map(int, input().split()))

# while dump_count > 0:
#     boxes = sorted(boxes)
#     boxes[-1] -= 1
#     boxes[0] += 1
#     dump_count -= 1
# print(boxes)
# print(f"#{1} {boxes[-1] - boxes[0]}")

# dump_count = int(input())
# boxes = list(map(int, input().split()))
# max_box = boxes[0]
# min_box = boxes[0]
# max_box_index = 0
# min_box_index = 0

# while dump_count > 0:
#     for box in range(100):
#         if boxes[box] > max_box:
#             max_box_index = box
#             max_box = boxes[box]
#         if boxes[box] < min_box:
#             min_box_index = box
#             min_box = boxes[box]

#     boxes[max_box_index] -= 1
#     boxes[min_box_index] += 1
#     dump_count -= 1

# for box in boxes:
#     if box > max_box:
#         max_box = box
#     if box < min_box:
#         min_box = box

# print(f"#{1} {max_box - min_box}")

# N, M = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(N)]
# max_sum = 0

# for row in range(N-M+1):
#     for col in range(N-M+1):
#         temp_sum = 0
#         for smash_row in range(M):
#             for smash_col in range(M):
#                 temp_sum += arr[row+smash_row][col+smash_col]

#         print(temp_sum, max_sum,'======================================')

#         if temp_sum > max_sum:
#             max_sum = temp_sum

# print(f"#{1} {max_sum}")


# arr = [list(map(int, input().split())) for _ in range(9)]
# print()
# print(arr)

# print(list(range(1,10)))


# arr = [list(map(int, input().split())) for _ in range(9)]
# check_num = list(range(1,10))
# check = 1

# for row in range(9):
#     check_list_row = []
#     check_list_col = []
#     for col in range(9):
#         check_list_row.append(arr[row][col])
#         check_list_col.append(arr[col][row])
#         if row % 3  == 0 and col % 3 == 0:
#             check_list_square = []
#             for square_row in range(3):
#                 for square_col in range(3):
#                     check_list_square.append(arr[row+square_row][col+square_col])

#     check_list_row = sorted(check_list_row)
#     check_list_col = sorted(check_list_col)
#     check_list_square = sorted(check_list_square)
#     print(check_list_row, check_list_col, check_list_square)

#     if check_list_row != check_num or check_list_col != check_num or check_list_square != check_num:
#         check = 0
#         break

# print(f"#{1} {check}")

T = int(input())
for tc in range(T):
    answer = 0
    numbers = []
    for i in range(9):
        numbers.append(list(map(int, input().split())))
 
    col_bool = True
    row_bool = True
    box_bool = True
    for i in range(9):
        col_arr = [0] * 10
        row_arr = [0] * 10
        box_arr = [0] * 10
        for j in range(9):
            if row_arr[numbers[i][j]] != 0:
                row_bool = False
            else:
                row_arr[numbers[i][j]] += 1
 
            if col_arr[numbers[j][i]] != 0:
                col_bool = False
            else:
                col_arr[numbers[j][i]] += 1
 
            if box_arr[numbers[int(i / 3) * 3 + int(j / 3)][(i % 3) * 3 + j % 3]] != 0:
                box_bool = False
            else:
                box_arr[numbers[int(i / 3) * 3 + int(j / 3)][(i % 3) * 3 + j % 3]] += 1
 
    if row_bool and col_bool and box_bool:
        answer = 1
    print(f'#{tc + 1} {answer}')