def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    cnt = 0

    for i in range(len(d)):
        budget -= d[i]
        cnt += 1

        if (budget < 0):
            cnt -= 1
            budget += d[i]
            break;

    answer = cnt
    return answer

# other solution
# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)

if __name__ == "__main__":
    # execute only if run as a script
    solution([1,3,2,5,4], 9)
    solution([2,2,3,3], 10)