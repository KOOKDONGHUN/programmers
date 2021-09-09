def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인
    if (x == 1):
        return False

    for i in range(2, x):
        # x가 해당 수로 나누어떨어지면
        if x % i == 0:
            return False
    return True

def permutation(arr, r):
    # 1.
    answer = []
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            # print(chosen)
            answer.append(chosen.copy())
            return chosen

        # 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return answer

def solution(numbers):
    answer = 0
    print(numbers)
    numbers = list(numbers)
    cnt = 0
    res = []

    for i in range(1, len(numbers)+1):
        t = permutation(numbers, i)
        # print(t)
        for j in t:
            aa = ''.join(j)

            if (len(aa) > 1):
                if (aa[0] == '0'):
                    aa = aa[1:]
                    if (len(aa) > 1):
                        if (aa[0] == '0'):
                            aa = aa[1:]
                            if (len(aa) > 1):
                                if (aa[0] == '0'):
                                    aa = aa[1:]
                                    if (len(aa) > 1):
                                        if (aa[0] == '0'):
                                            aa = aa[1:]

            res.append(aa)
    res = list(set(res))

    if ('0' in res):
        res.remove('0')
    if ('1' in res):
        res.remove('1')

    print(res)

    for i in res:
        if (is_prime_number(int(i))):
            cnt += 1
    answer = cnt
    print(answer)
    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution("17")
    print('-'*33)
    solution("011")
