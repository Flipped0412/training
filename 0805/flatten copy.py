for test_case in range(1, 11):
    dump_count = int(input())
    boxes = list(map(int, input().split()))

    while dump_count > 0:
        boxes = sorted(boxes)
        boxes[-1] -= 1
        boxes[0] += 1
        dump_count -= 1

    boxes = sorted(boxes)
    
    print(f"#{test_case} {boxes[-1] - boxes[0]}")