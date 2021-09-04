def grade(total_win_cnt):
    if (total_win_cnt == 6):
        return 1
    elif (total_win_cnt == 5):
        return 2
    elif (total_win_cnt == 4):
        return 3
    elif (total_win_cnt == 3):
        return 4
    elif (total_win_cnt == 2):
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    # list calc minus [x - y] sample
    # [item for item in x if item not in y]
    answer = []

    loss_num = [item for item in win_nums if item not in lottos]
    print(loss_num)

    zero_cnt = lottos.count(0)
    print(f"zero_cnt :: {zero_cnt}")
    win_cnt = 6 - len(loss_num)

    max_grade = grade(win_cnt + zero_cnt)
    min_grade = grade(win_cnt)

    answer.append(max_grade)
    answer.append(min_grade)

    return answer

# others solution ... wow
# def solution(lottos, win_nums):
#
#     rank=[6,6,5,4,3,2,1]
#
#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]

if __name__ == "__main__":
    # execute only if run as a script
    solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
    solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
    solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])