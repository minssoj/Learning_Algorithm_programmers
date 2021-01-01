def solution(brown, yellow):
    b = int((brown - 4) / 2)  # w+h
    y = int(yellow)  # wh

    for i in range(1, b):
        h = i
        w = b - i
        if y == h * w:
            break

    answer = [w + 2, h + 2]
    return answer