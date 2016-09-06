__author__ = 'Josh'


def main():
    encrypted = "HUMXZLTUFXLLFXDDVMYTMTOSEKAGLFRIWFFSBRORVHLFGVXAVNXOSWFAVUHYUXBFAWWEMMANSKWSJJFVGRAYMRNG"
    print(encrypted)
    matrix = grid_generator(encrypted)
    grid_printer(matrix)


def grid_printer(matrix):
    """
    pretty prints the matrix grid
    :param matrix: The encrypted message grid
    :return: None
    """
    for x in matrix:
        print(x)


def grid_generator(encrypted):
    """
    Generates the 'grid' of offset encrypted text
    :param encrypted: The encrypted message
    :return: returns a matrix that is primed for the coincidences counter
    """
    matrix = []
    for x in range(len(encrypted)):
        tempStr = " " * x
        tempStr += encrypted[x:]
        matrix.append(tempStr)
    return matrix


if __name__ == "__main__":
    main()