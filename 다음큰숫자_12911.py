def solution(n):
    bi = bin(n)[2:]
    num_1 = bi.count('1')
    number = n + 1
    while True:
        nbi = bin(number)[2:]
        nnum_1 = nbi.count('1')
        if num_1 == nnum_1:
            break
        number += 1

    return number