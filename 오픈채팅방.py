def solution(record):
    answer = []
    nick = {}

    for rec in record:
        rec_l = rec.split(" ")

        # 닉네임 저장
        if rec_l[0] != 'Leave':  # Enter 및 change의 경우 닉네임 변경
            nick[rec_l[1]] = rec_l[2]

    for rec in record:
        rec_l = rec.split(" ")

        if rec_l[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(nick[rec_l[1]]))
        elif rec_l[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(nick[rec_l[1]]))

    return answer