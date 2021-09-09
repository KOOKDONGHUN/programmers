from itertools import product


def solution(word):
    answer = 0

    answer_ = []

    for i in product("AEIOU", "AEIOU", "AEIOU", "AEIOU", "AEIOU"):
        answer_.append(''.join(list(i)))

    for i in product("AEIOU", "AEIOU", "AEIOU", "AEIOU"):
        answer_.append(''.join(list(i)))

    for i in product("AEIOU", "AEIOU", "AEIOU"):
        answer_.append(''.join(list(i)))

    for i in product("AEIOU", "AEIOU"):
        answer_.append(''.join(list(i)))

    for i in product("AEIOU"):
        answer_.append(''.join(list(i)))

    answer_.sort()

    answer = answer_.index(word) + 1

    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution("AAAAE")
    solution("AAAE")
    solution("I")
    solution("EIO")