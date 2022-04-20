"""
# 1 Binary Search
# 2 Linear Search
"""

# #####################################################################################

1) BINARY SEARCH

                         Theory

Binary search is an efficient algorithm for finding an item
from sorted list of items. It works by repeatedly dividing in
half the portion of the list that could contain the item
until you have narrowed down the possible locations to just one.


                      Source Code


def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        mid_point = begin_index + (end_index - begin_index) // 2
        mid_point_value = sequence[mid_point]

        if mid_point_value == item:
            return mid_point

        elif item < mid_point_value:
            end_index = mid_point - 1

        else:
            begin_index = mid_point + 1

    return None


sequence_a = [2, 3, 5, 7, 9, 12, 13, 15, 22]
item_a = 7

print(binary_search(sequence_a, item_a))







