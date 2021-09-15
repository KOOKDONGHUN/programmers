def check_t(s):
    op1 = 0
    op2 = 0
    op3 = 0

    for idx in range(len(s)):
        if (s[idx] == "("):
            op1 += 1
        elif (s[idx] == ")"):
            op1 -= 1

        if (s[idx] == "["):
            op2 += 1
        elif (s[idx] == "]"):
            op2 -= 1

        if (s[idx] == "{"):
            op3 += 1
        elif (s[idx] == "}"):
            op3 -= 1

        if (op1 < 0 or op2 < 0 or op3 < 0):
            return False

    if (op1 == 0 and op2 == 0 and op3 == 0):
        return True
    else:
        return False

def check_t2(s):
    st = []

    for idx in range(len(s)):
        k = s[idx]
        if (k == "(" or s[idx] == "[" or s[idx] == "{"):
            st.append(k)

        elif (len(st)==0 and (k == ")" or k == "]" or k == "}")):
            return False

        elif (k == ")"):
            if (len(st)):
                if (st[-1] == "("):
                    st.pop()
                else:
                    return False

        elif (k == "]"):
            if (len(st)):
                if (st[-1] == "["):
                    st.pop()
                else:
                    return False

        elif (k == "}"):
            if (len(st)):
                if (st[-1] == "{"):
                    st.pop()
                else:
                    return False
    return True

def solution(s):
    answer = 0

    if (len(s) == 1):
        return 0

    if (len(s)%2 == 1):
        return 0

    if (check_t2(s)):
        answer += 1

    for i in range(1, len(s)):
        t = s[i:] + s[0:i]
        if (check_t2(t)):
            answer += 1
    print(answer)
    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution("[](){}")
    solution("}]()[{")
    solution("[)(]")
    solution("}}}")
    solution("{]")