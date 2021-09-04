def solution(absolutes, signs):
    answer = 0

    for idx in range(len(absolutes)):
        if (signs[idx] == False):
            absolutes[idx] = absolutes[idx] * -1
        answer += absolutes[idx]

    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution([4,7,12], [True,False,True])
    solution([1,2,3], [False,False,True])

## Perfect