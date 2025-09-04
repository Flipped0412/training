def KFC(x):
    print(x)
    x += 3
    BBQ(x + 2)
    print(x)


def BBQ(x):
    x += 10
    print(x)


x = 3
KFC(x + 1)
print(x)