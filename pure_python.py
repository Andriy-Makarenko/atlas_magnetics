from __future__ import annotations

data_set = [364, 373, 358, 394, 378, 379, 357, 364, 350,
            363, 392, 368, 359, 375, 399, 365, 379, 357, 380]


def data_validation(data: list):
    if len(data) == 0:
        return "Empty list"
    if not all(isinstance(number, (int, float)) for number in data):
        return "Not all values in list are numerical"

    return False


def mean(data: list) -> float:
    """Calculate mean value using cycle"""
    if data_validation(data):  # input data validation
        return data_validation(data)
    result = 0
    length = 0

    for number in data:
        result += number  # sum of all set values
        length += 1  # number of values it the set

    return result / length


def mean2(data: list) -> float | str:
    """Calculate mean value using built-in sum and len functions"""
    if data_validation(data):  # input data validation
        return data_validation(data)

    return sum(data) / len(data)


def median(data: list) -> float | str:
    if data_validation(data):  # input data validation
        return data_validation(data)
    data.sort()

    if len(data) % 2 != 0:  # for odd length list median number in the middle
        return data[len(data) // 2]

    # for even length list median number between two middle values
    return (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2


def mode(data: list) -> list | str:
    if data_validation(data):  # input data validation
        return data_validation(data)
    unique_values = set(data_set)  # unique values of data
    result = []

    for number in unique_values:
        count = data.count(number)  # count each number appearance in the data
        if count > 1:
            # add only numbers appeared more than once
            result.append((number, count))
    #  sort list tuples by count value
    result.sort(reverse=True, key=lambda item: item[1])

    if not result:  # if result is an empty list
        return "List doesn't have mode values"
    # all value-count tuple pair with equal number
    # of value appearance in the data
    return [
        number_count_pair
        for number_count_pair in result
        if number_count_pair[1] == result[0][1]
    ]


def standard_deviation(data: list) -> list | str:
    if data_validation(data):  # input data validation
        return data_validation(data)

    # mean value of the data set
    mean_value = mean2(data)
    # sum of squared difference from mean value to each data point
    deviation_sum = sum((mean_value - number) ** 2 for number in data)
    # average deviation sum
    avg_deviation_sum = deviation_sum / len(data)

    return avg_deviation_sum ** 0.5  # square root of average deviation sum


print(
    f"mean - {mean(data_set)}",
    f"mean2 - {mean2(data_set)}",
    f"median - {median(data_set)}",
    f"mode - {mode(data_set)}",
    f"standard deviation - {standard_deviation(data_set)}",
    sep="\n",
)
