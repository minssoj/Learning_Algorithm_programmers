# 참고 : (https://velog.io/@ckstn0777/)
def solution(board):
    width = len(board[0])  # 너비
    height = len(board)  # 높이

    # (1,1) 부터 시작함
    for x in range(1, height):
        for y in range(1, width):
            if board[x][y] == 1:
                # 자신을 기준으로 위, 왼쪽, 왼쪽 상단에서 최솟값 + 1을 해준다
                board[x][y] = (
                    min(board[x - 1][y - 1], board[x - 1][y], board[x][y - 1]) + 1
                )

    return max([item for row in board for item in row]) ** 2