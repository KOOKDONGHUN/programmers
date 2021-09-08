def solution(weights, head2head):
    answer = []

    # 1. 승률순서대로 정렬
    score_ls = []
    for i in head2head:
        win_cnt = i.count('W')
        no_cnt = i.count('N')
        loss_cnt = i.count('L')

        if (win_cnt + loss_cnt) != 0:
            score_ls.append((win_cnt*100)/(win_cnt+loss_cnt))
        else:
            score_ls.append(0)

        # if (no_cnt >= (len(i)-1)):
        #     score_ls.append(0)
        # else:
        #     score_ls.append(win_cnt / (len(i)-no_cnt))

    # 2. 몸무게가 많은 사람을 이긴 횟수
    over_w_cnt_ls = list()
    for i in range(len(head2head)):
        over_w_cnt = 0
        for j in range(len(head2head[i])):
            if (head2head[i][j] == 'W') :
                if (weights[i] < weights[j]) :
                    over_w_cnt += 1
        over_w_cnt_ls.append(over_w_cnt)

    # for idx, w in enumerate(weights):
    #     over_w_cnt = 0
    #     over_w_ls = list(filter(lambda x : x>w, weights))
    #     for over_w in over_w_ls:
    #         if (head2head[idx][weights.index(over_w)] == 'W'):
    #             over_w_cnt += 1
    #     over_w_cnt_ls.append(over_w_cnt)
    # print(over_w_cnt_ls)

    # 3. 자기 몸무게가 더 무거운 사람 순서

    # 4. 등번호? 가 작은 사람이 앞쪽
    num_ls = [i for i in range(1,len(weights)+1)]

    tot = [i for i in zip(score_ls, over_w_cnt_ls, weights, num_ls)]
    # head2head_cat_ls = [i for i in zip(score_ls, over_w_cnt_ls, weights, num_ls)]
    for i in range(len(tot)-1):
        for j in range(len(tot)-i-1):
            if (tot[j][0] < tot[j + 1][0]):
                temp = tot[j]
                tot[j] = tot[j + 1]
                tot[j + 1] = temp
            elif (tot[j][0] == tot[j + 1][0]):
                if (tot[j][1] < tot[j + 1][1]):
                    temp = tot[j]
                    tot[j] = tot[j + 1]
                    tot[j + 1] = temp
                elif(tot[j][1] == tot[j + 1][1]):
                    if(tot[j][2] < tot[j + 1][2]):
                        temp = tot[j]
                        tot[j] = tot[j + 1]
                        tot[j + 1] = temp
                    elif (tot[j][2] == tot[j + 1][2]):
                        if (tot[j][3] > tot[j + 1][3]):
                            temp = tot[j]
                            tot[j] = tot[j + 1]
                            tot[j + 1] = temp
    # head2head_cat_ls = sorted(head2head_cat_ls, key=lambda x : (x[0], x[1], x[2], -x[3]), reverse=True)

    print(tot)
    # print(head2head_cat_ls)

    last_ls = []
    # for i in head2head_cat_ls:
    #     last_ls.append(i[-1])

    for i in tot:
        last_ls.append(i[-1])

    # # 찐막
    # ll = []
    # for i in weights:
    #     ll.append(last_ls.index(i)+1)
    #
    # answer = ll

    print(last_ls)

    answer = last_ls

    return answer

# others solution
# def solution(weights, head2head):
#     answer = []
#     arr =[]
#     for i in range(len(head2head)):
#         rate = 0
#         lose = 0
#         win = 0
#         weight_win=0
#         for j in range(len(head2head)):
#             if i==j:
#                 continue
#
#             if head2head[i][j] == "L":
#                 lose += 1
#
#             elif head2head[i][j] == "W":
#                 win += 1
#
#                 if weights[i] < weights[j]:
#                     weight_win += 1
#         if (win+lose) != 0:
#             rate = (win*100)/(win+lose)
#         else:
#             rate = 0
#         arr.append([rate, weight_win, weights[i], -(i+1)])
#
#         arr.sort(reverse=True)
#
#     answer = [-x[-1] for x in arr]
#
#
#     return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])
    solution([145,92,86], ["NLW","WNL","LWN"])
    solution([60,70,60], ["NNN","NNN","NNN"])
