from datetime import datetime
import math

def solution(fees, records):
    answer = []
    t_ls = []
    car_num_ls = []
    check_ls = []
    car_num_ls2 = []
    minute = 60
    dead_line = "23:59"

    log = dict()

    for record in records:
        t, car_num, check = record.split()
        t_ls.append(t)
        car_num_ls.append(car_num)
        check_ls.append(check)

        if (car_num not in car_num_ls2):
            car_num_ls2.append(car_num)

    for num in car_num_ls:
        log[f'{num}'] = []

    for idx in range(len(car_num_ls)):
        log[f'{car_num_ls[idx]}'].append(t_ls[idx])

    # print(log)

    time_log = dict()

    for key, value in log.items():
        time_log[f'{key}'] = []
        l = len(value)
        if (l % 2 == 1):
            st = ''
            for i in range(l-1):
                if (i % 2 == 1): # out
                    a = datetime.strptime(st, '%H:%M')
                    b = datetime.strptime(value[i], '%H:%M')
                    c = (b - a).seconds/60
                    time_log[f'{key}'].append(c)
                else: # in
                    st = value[i]
            # 마지막 하나 연산 마감시간까지 하는거
            a = datetime.strptime(value[-1], '%H:%M')
            b = datetime.strptime(dead_line, '%H:%M')
            c = (b - a).seconds / 60
            time_log[f'{key}'].append(c)
        else:
            st = ''
            for i in range(l):
                if (i % 2 == 1):  # out
                    a = datetime.strptime(st, '%H:%M')
                    b = datetime.strptime(value[i], '%H:%M')
                    c = (b - a).seconds / 60
                    time_log[f'{key}'].append(c)
                else:  # in
                    st = value[i]
    # print(time_log)

    answer2 = dict()
    for key, value in time_log.items():
        answer2[f'{key}'] = 0
        if (sum(value) <= fees[0]):
            answer2[f'{key}'] = fees[1]
        else:
            r1 = int(sum(value)) - fees[0]
            r2 = math.ceil(r1 / fees[2])
            r3 = r2 * fees[3]
            rr = fees[1] + r3
            answer2[f'{key}'] = rr

    answer = []
    car_num_ls2.sort()
    for i in car_num_ls2:
        answer.append(answer2[i])
    # print(answer)
    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
    print('-'*38)
    solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
    print('-' * 38)
    solution([1, 461, 1, 10], ["00:00 1234 IN"])