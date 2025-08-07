for test_case in range(1, 11):
    dump_count = int(input())
    boxes = list(map(int, input().split()))

    while dump_count > 0:
        max_box_index = 0
        min_box_index = 0

        for box in range(100):
            if boxes[box] > max_box:
                max_box_index = box
            if boxes[box] < min_box:
                min_box_index = box

        boxes[max_box_index] -= 1
        boxes[min_box_index] += 1
        dump_count -= 1

    max_box = boxes[0]
    min_box = boxes[0]

    for box in boxes:
        if box > max_box:
            max_box = box
        if box < min_box:
            min_box = box

    print(f"#{test_case} {max_box - min_box}")
