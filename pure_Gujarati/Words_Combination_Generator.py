def combinationUtil(arr, n, r, index, data, i, final_data):
    if index == r:
        final_data.append(data.copy())
        return
    if i >= n:
        return

    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1, data, i + 1, final_data)
    combinationUtil(arr, n, r, index, data, i + 1, final_data)


def getCombination(arr, n, r):
    """

    :param arr: list of words
    :param n: total words
    :param r: number os selection
    :return: list of possibilities
    """
    data = [0] * r
    final_data = list()  # works as a single list in whole execution LIKE A POINTER IN C/C++
    # PYTHON IS PRETTY AWESOME RIGHT !!!

    combinationUtil(arr, n, r, 0, data, 0, final_data)
    return final_data


def factorial_word_selection(words_list):
    """

    :param words_list: list
        list of words
    :return: list
        list of all possible factorial possibilities
    """
    n = len(words_list)
    possibility = list()
    for i in range(1, n+1):
        possibility.append(getCombination(words_list, n, i)[0:n])
    return possibility


'''
l = list()
l.extend("Trus")
print(l)

factorial_word_selection(l)
'''
