__author__ = 'Josh'
import string


def main():
    encrypted = "HUMXZLTUFXLLFXDDVMYTMTOSEKAGLFRIWFFSBRORVHLFGVXAVNXOSWFAVUHYUXBFAWWEMMANSKWSJJFVGRAYMRNG"
    print(encrypted)
    matrix = grid_generator(encrypted)
    grid_printer(matrix)
    coincidence_list = coincidence_finder(encrypted, matrix)
    print(coincidence_list)
    print(percentage_maker(encrypted, 2))


def percentage_maker(encrypted, keyLength):
    """
    Takes in the encrypted message and the key length and creates a frequency percentage
    :param encrypted: The encrypted message.
    :param keyLength: The length of the key.
    :return: A list of percents for how often a letter occurs
    """
    freq_dict = {letter: 0 for letter in string.ascii_uppercase}

    for x in range(len(encrypted)):
        if x % keyLength == 0:
            freq_dict[encrypted[x]] += 1

    percent_list = []
    for letter in string.ascii_uppercase:
        percent_list.append(freq_dict[letter] / len(encrypted))

    return percent_list


def coincidence_finder(encrypted, matrix):
    """
    Calculates the number of coincidences per possible string
    :param encrypted: The encrypted message
    :param matrix: The grid of shifted messages
    :return: The list of coincidences in order, used to determine the key length.
    """
    coincidence_list = []
    for offset in matrix:
        tempCount = 0
        for x in range(len(encrypted)):
            if offset[x] == encrypted[x]:
                tempCount += 1
        coincidence_list.append(tempCount)
    return coincidence_list

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
        tempStr += encrypted[:len(encrypted) - x]
        matrix.append(tempStr)
    return matrix


if __name__ == "__main__":
    main()