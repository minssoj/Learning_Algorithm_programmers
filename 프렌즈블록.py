def solution(m, n, board):
    x = board
    x2 = [list(i) for i in x]

    # 지워 보기
    point = 1
    while point != 0:
        list_array = []  # 지워질 블록의 목록 (위쪽 좌측좌표)
        point = 0
        for i in range(m - 1):
            # 열
            for j in range(n - 1):
                # 자신을 기준으로 오른쪽, 밑, 오른쪽 밑이 전부 같고, '-'가 아니라면
                if x2[i][j] == x2[i][j + 1] == x2[i + 1][j] == x2[i + 1][j + 1] != "-":
                    list_array.append([i, j])
                    point += 1

        # 지워질 블록들 -로 바꾸기
        for i2 in list_array:
            i, j = i2[0], i2[1]
            x2[i][j], x2[i][j + 1], x2[i + 1][j], x2[i + 1][j + 1] = (
                "-",
                "-",
                "-",
                "-",
            )

        # '-'를 제일 위로 보내기 위해서 반복처리
        # 충분히 반복문을 돌리기위해서 m만큼 반복처리함.
        for _ in range(m):
            # 행
            for i in range(m - 1):
                # 열
                for j in range(n):
                    # 자신의 아래가 '-'라면 그 둘의 순서를 바꿔줌
                    if x2[i + 1][j] == "-":
                        x2[i + 1][j], x2[i][j] = x2[i][j], "-"

    # 지워진 개수 찾기 (-)
    answer = 0
    for i in x2:
        answer += i.count("-")
    return answer