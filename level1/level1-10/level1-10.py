def calc_position(n):
    a = n // 3
    b = (n % 3) - 1

    if (b < 0):
        b = 2
        a -= 1

    return a,b

def calc_distance(i1,j1, i2, j2):

    return abs(i1 - i2) + abs(j1 - j2)


def solution(numbers, hand):
    answer = ""

    l = 0

    if (hand == "right"):
        hand = 'R'
    elif (hand == "left"):
        hand = 'L'
        l = 1

    lh = 10
    rh = 12

    for n in numbers:
        if (n == 0):
            n = 11

        i1, j1 = calc_position(n)

        if (j1 == 0):
            answer += 'L'
            lh = n
        elif(j1 == 2):
            answer += 'R'
            rh = n
        else:
            i2,j2 = calc_position(lh)
            i3,j3 = calc_position(rh)

            ld = calc_distance(i1, j1, i2, j2)
            rd = calc_distance(i1, j1, i3, j3)

            if (ld > rd):
                answer += 'R'
                rh = n
            elif (ld < rd):
                answer += 'L'
                lh = n
            else:
                answer += hand

                if (l):
                    lh = n
                else:
                    rh = n

    print(answer)
    return answer

# 다른 사람 풀이보다 이거는 내께 가장 깔끔하지 않았나 ... 자부심 ...

if __name__ == "__main__":
    # execute only if run as a script
    solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")

    solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")

    solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")