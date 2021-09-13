def solution(id_list, report, k):
    answer = []

    k_cnt = dict()
    user_sub = dict()
    answer = dict()

    for id in id_list:
        k_cnt[f'{id}'] = 0
        user_sub[f'{id}'] = []
        answer[f'{id}'] = 0

    for rep in report:
        user1, user2 = rep.split(" ")
        if (user1 not in user_sub[f'{user2}']):
            k_cnt[f'{user2}'] = k_cnt[f'{user2}'] + 1
            user_sub[f'{user2}'].append(user1)

    # print(k_cnt)
    # print(user_sub)

    for key, v in k_cnt.items():
        if (v >= k):
            # answer[key] = answer[key] + 1
            for j in user_sub[key]:
                answer[j] = answer[j] + 1

    # print(answer)
    # print(k_cnt)
    # print(user_sub)
    answer = list(answer.values())
    # print(answer)
    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
    print('-'*38)
    solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)