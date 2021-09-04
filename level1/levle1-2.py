def grade(score):
    if (score >= 90):
        return 'A'
    elif (score >= 80):
        return 'B'
    elif (score >= 70):
        return 'C'
    elif (score >= 50):
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    print(scores)
    # transpose
    scores = [list(x) for x in zip(*scores)]
    print(scores)
    for i in range(len(scores)):
        ss = scores[i]
        ans = 0
        if (ss[i] == min(ss)):
            cnt = 0
            for kk in ss:
                if (kk == min(ss)):
                    cnt += 1
            if (cnt > 1):
                ans = sum(ss) / len(ss)
            else:
                ans = (sum(ss) - ss[i]) / (len(ss) - 1)
                print(f"ans :: {ans} ", end='')

        elif (ss[i] == max(ss)):
            cnt = 0
            for kk in ss:
                if (kk == max(ss)):
                    cnt += 1
            if (cnt > 1):
                ans = sum(ss) / len(ss)
            else:
                ans = (sum(ss) - ss[i]) / (len(ss) - 1)
                print(f"ans :: {ans} ", end='')
        else:
            ans = sum(ss) / len(ss)
        print(f"ans :: {ans}, idx :: {i}, ss[i] :: {ss[i]}")
        answer += grade(ans)

    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])
    solution([[50,90],[50,87]])
    solution([[70,49,90],[68,50,38],[73,31,100]])