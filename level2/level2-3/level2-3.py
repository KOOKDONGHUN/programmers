def solution(record):
    answer = []

    d = dict()
    for rec in record:
        t = rec.split(" ")
        if (t[0] == "Enter" or t[0] == "Change"):
            d[f'{t[1]}'] = t[2]

    for rec in record:
        t = rec.split(" ")
        if (t[0] == "Enter"):
            answer.append(f"{d[f'{t[1]}']}님이 들어왔습니다.")
        elif (t[0] == "Leave"):
            answer.append(f"{d[f'{t[1]}']}님이 나갔습니다.")
    # print(answer)
    return answer

# others solutions
# def solution(record):
#     answer = []
#     namespace = {}
#     printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
#     for r in record:
#         rr = r.split(' ')
#         if rr[0] in ['Enter', 'Change']:
#             namespace[rr[1]] = rr[2]
#
#     for r in record:
#         if r.split(' ')[0] != 'Change':
#             answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
#
#     return answer

# def solution(record):
#     user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
#     return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]


if __name__ == "__main__":
    # execute only if run as a script
    solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
              "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

