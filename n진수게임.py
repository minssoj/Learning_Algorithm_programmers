num_ = ["A", "B", "C", "D", "E", "F"]  # 10, 11, 12, 13, 14, 15


def solution(n, t, m, p):
    l = ''
    i = 0
    while True:
        if len(l) >= t * m:
            break
        # 숫자마다 이진법 변환하여 붙이기
        num_l = ""
        num = i
        # 진법변환
        if num == 0:
            l = '0' + l
            i += 1
            continue
        while num:
            if num % n > 9:
                num_l = num_[num % n - 10] + num_l
            else:
                num_l = str(num % n) + num_l
            num = num // n
        l = l + num_l
        i += 1

    # m주기로 t만큼
    answer = l[p - 1::m][:t]
    return answer