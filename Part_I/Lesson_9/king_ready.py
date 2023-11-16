def draw_field(init, target):
    for i in range(8):
        for j in range(8):
            if i == init[0] and j == init[1]:
                print("k", end="  ")
            elif i == target[0] and j == target[1]:
                print("t", end="  ")
            else:
                print("0", end="  ")
        print()
    if abs(init[0]-target[0]) + abs(init[1]-target[1]) == 1:
        print(True)
        return True
    elif abs(init[0]-target[0]) + abs(init[1]-target[1]) == 2 \
            and abs(init[0]-target[0]) != 0 and abs(init[1]-target[1]) != 0:
        print(True)
        return True
    else:
        print(False)
        return False


draw_field((4, 5), (3, 7))
