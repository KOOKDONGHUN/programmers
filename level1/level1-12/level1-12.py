def solution(board, moves):
    answer = 0

    # transpose
    board = [list(x)for x in zip(*board)]

    # 뽑은 인형 리스트
    res = []

    for lane in moves:
        # 칸에서 인형을 다 뽑아서 없는 경우
        if (board[lane-1] == []):
            continue

        # 0이 아닐때까지 계속 뽑기
        while True:
            a = board[lane-1].pop(0)
            if (a != 0):
                break

        res.append(a)

    # 뽑은 인형의 총 개수
    org_len = len(res)

    # 터트릴수 있는건 최소 2개이상이 존재 해야 하기 때문
    while (len(res) >= 2):
        temp = len(res)

        # 2개가 연속으로 있는 경우 제거
        for i in range(temp-1):
            if (res[i] == res[i+1]):
                res.pop(i + 1)
                res.pop(i)
                break

        # 끝까지 다 갔는데 터지지 않은경우 종료
        if (i == temp-2):
            break

    # 터트려진 인형 = 전체 인형 - 남아 있는 인형
    answer = org_len - len(res)

    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])