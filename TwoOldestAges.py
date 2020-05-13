"""
The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items.

For example:

two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]

"""


def two_oldest_ages(ages):
    max_one = []
    max_two = []
    my_list = []

    max_one = max(ages)
    ages.remove(max_one)
    max_two = max(ages)

    my_list.append(max_two)
    my_list.append(max_one)

    return my_list
