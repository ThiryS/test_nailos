def array_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(array_sum([1, 2, 3, 4, 5]))


def array_sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + array_sum_recursive(numbers[1:])


print(array_sum_recursive([1, 2, 3, 4, 5]))
