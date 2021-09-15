def solution(n, lost, reserve):
    # 총 학생 수 n
    # 체육복이 없는 학생 lost
    # 여벌 체육복이 있는 학생 reserve
    # lost에 있는 학생은 앞뒤로만 빌릴수 있음

    c = [item for item in reserve if item not in lost]
    d = [item for item in lost if item not in reserve]

    c.sort()
    d.sort()

    cnt = n - len(d)

    for i in d:
        a = i-1
        b = i+1

        if (a in c):
            c.remove(a)
            cnt += 1
        elif (b in c):
            c.remove(b)
            cnt += 1

    return cnt

# others solutions ## 이 사람은 잃어버린 사람의 리스트로 최종 인원을 구했다 ...
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)

if __name__ == "__main__":
    # execute only if run as a script
    solution(5, [2, 4], [1, 3, 5])
    solution(5, [2, 4], [3])
    solution(3, [3], [1])