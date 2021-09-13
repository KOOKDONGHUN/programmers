import string

tmp = string.digits+string.ascii_lowercase

def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인
    if (x == 1):
        return False

    for i in range(2, x):
        # x가 해당 수로 나누어떨어지면
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    con = n
    if (k != 10):
        con = str(convert(n, k))

    # if (is_prime_number(int(''.join(tt)))):
    #     answer += 1
    t = []
    tt = ''
    for idx in range(len(con)):
        i = con[idx]

        tt += i

        if (len(tt) > 2):
            if ('0' in tt[1:-1]):
                tt = ''
            else:
                if (idx + 1 < len(con)):
                    if (con[idx + 1] == '0'):
                        t.append(tt)
                        tt = ''
                else:
                    t.append(tt)
                    tt = ''
        else:
            if (con[idx+1] == '0'):
                t.append(tt)
                tt = ''
            # else:
    answer = []
    for i in t:
        if (i == '0' or i == '00'):
            continue
        while(i[0] == '0'):
            i = i[1:]
        answer.append(i)

    res = 0

    for i in answer:
        if (is_prime_number(int(i))):
            res += 1

    # print(con)
    # print(t)
    # print(answer)
    answer = res
    # print(answer)

    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution(437674, 3)
    print('-'*38)
    solution(110011, 10)