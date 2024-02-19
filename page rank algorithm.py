def scalar_mtrx_mult(scalar, M):
    # M- matrix
    # scalar - a float number
    # multiplying matrix by scalar
    result = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            result[i][j] = scalar * M[i][j]
    return result


def mtrx_add(M, N):
    # M- first matrix
    # N-  second matrix
    # addition pf two matrix
    if len(M) != len(N) or len(M[0]) != len(N[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    result = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            result[i][j] = M[i][j] + N[i][j]
    return result


def mtrx_mult(M, N):
    # M- first matrix
    # N-  second matrix
    # muliplication pf two matrix
    result = [[0 for _ in range(len(N[0]))] for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(N)):
                result[i][j] += M[i][k] * N[k][j]
    return result


def pageRank(tax, M, n):
    # tax - precent of reaching a dead end or spider trap and launching at a differernt page
    # M - given matrix
    # n - number of iteration we would like to calculate

    beta = 1 - tax
    M_size = len(M)
    page_rank = [[1 / M_size]] * M_size
    p_initial = scalar_mtrx_mult(tax, page_rank)
    for i in range(n):
        page_rank = mtrx_add(scalar_mtrx_mult(beta, mtrx_mult(M, page_rank)), p_initial)
        print(page_rank)
    return page_rank


def main():
    print(
        pageRank(0.2, [[0.0, 0.0, 0.0, 1.0], [1/2, 0.0, 0.0, 0.0], [1/2, 0.0, 0.0, 0.0], [0.0, 1, 1, 0.0]],
                 2001))

    return


if __name__ == "__main__":
    main()
