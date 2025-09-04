# bit = [0] * 4
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)



def made(a):
    if a >= N:
        print(bit)
        return

    for i in range(2):
        bit[a] = i
        made(a+1)


N = 4
bit = [0] * N

made(0)
