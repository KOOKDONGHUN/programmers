def solution(rows, columns, queries):
    answer = []

    mat = []
    mat_c = []
    temp = []


    for i in range(1, rows*columns+1):
        if (i%columns == 0):
            temp.append(i)
            mat.append(temp)
            temp = []
        else:
            temp.append(i)

    mat_c = []

    for i in mat:
        mat_c.append(i[:])

    for x1, y1, x2, y2 in queries:
        m = float("inf")
        for j in range(x1-1, x2):
            for k in range(y1-1, y2):
                if (abs(x2-x1) < 2 or abs(y2-y1) < 2):
                    # print(f"{j},{k}", end=" => ")
                    if (k == y1 - 1 and x1 - 1 <= j and j < x2 - 1):
                        mat[j][k] = mat_c[j + 1][k]
                        # print(f"{j + 1},{k}")
                    elif (j == x1 - 1 and y1 - 1 < k and k <= y2 - 1):
                        mat[j][k] = mat_c[j][k -1]
                        # print(f"{j},{k - 1}")
                    elif (x1 - 1 < j and j <= x2 - 1 and k == y2 - 1):
                        mat[j][k] = mat_c[j - 1][k]
                        # print(f"{j - 1},{k}")
                    else:
                        mat[j][k] = mat_c[j][k + 1]
                        # print(f"{j},{k + 1}")
                    # min
                    if (m >= mat[j][k]):
                        m = mat[j][k]
                else:
                    if not(x1 <= j and j <= x2-2 and y1 <= k and k <= y2-2):
                        # print(f"{j},{k}", end=" => ")
                        if (k == y1 - 1 and x1 - 1 <= j and j < x2 - 1):
                            mat[j][k] = mat_c[j + 1][k]
                            # print(f"{j + 1},{k}")
                        elif (j == x1 - 1 and y1 - 1 < k and k <= y2 - 1):
                            mat[j][k] = mat_c[j][k - 1]
                            # print(f"{j},{k - 1}")
                        elif (x1 - 1 < j and j <= x2 - 1 and k == y2 - 1):
                            mat[j][k] = mat_c[j - 1][k]
                            # print(f"{j - 1},{k}")
                        else:
                            mat[j][k] = mat_c[j][k + 1]
                            # print(f"{j},{k + 1}")
                        # min
                        if (m >= mat[j][k]):
                            m = mat[j][k]

        answer.append(m)
        mat_c.clear()
        for ll in mat:
            mat_c.append(ll[:])

    # print(answer)
    return answer

if __name__ == "__main__":
    # execute only if run as a script
    solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
    solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
    solution(100, 97, [[1,1,100,97]])