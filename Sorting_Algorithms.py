"""
1 Bubble sort
2 Selection sort
3 Insertion sort
4 Quick sort
5 Merge sort
6 Heap sort
7 Radix sort
"""


#######################################################################

1) BUBBLE SORT

                                - Theory
It works by repeatedly swapping the adjacent
element if they're in wrong order



                                - Source Code
def sort_num(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                box = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = box


numbers = [2, 6, 3, 1, 4, 5]
sort_num(numbers)
print(numbers)



#########################################################################################


2) SELECTION SORT

                        - Theory
It divides the array into 2 parts, left part is sorted and
right part is unsorted. This algorithm sorts the array by
repeatedly finding the MINIMUM element (Compares with each element)
from unsorted part and putting it at the end (sorted part)


                        - Source code
def sort_num(numbers):

    for i in range(5):
        minimum = i
        for j in range(i, 6):
            if numbers[j] < numbers[minimum]:
                minimum = j

        box = numbers[i]
        numbers[i] = numbers[minimum]
        numbers[minimum] = box



numbers = [2, 6, 3, 1, 4, 5]
sort_num(numbers)
print(numbers)


def selection_sort(numbers):
    for i in range(0, len(numbers) - 1):
        min_value = i

        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_value]:
                min_value = j

        if min_value != i:
            numbers[min_value], numbers[i] = numbers[i], numbers[min_value]

    return numbers

print(selection_sort([2, 6, 1, 5, 4, 3]))

#########################################################################################


3) INSERTION SORT

                            -Theory

Here the array is virtually split into a sorted and
unsorted part. In sorted part will be first element
and other elements will be added to sorted part one by one
And compared with elements in sorted part, if they're in wrong
order, they'll be swapped


                            -Source code

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        value_to_sort = numbers[i]

        while numbers[i - 1] > value_to_sort and i > 0:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            i -= 1

    return numbers

print(insertion_sort([3, 5, 2, 4, 1]))


######################################################################################


4) Quick Sort

PIVOT is a number that we want to base the
comparison with all other numbers

                            -Theory
It'll take any element as PIVOT element, then
divides the array into lower and greater sides, then
PIVOT element will be compared with each element,
if element is greater than PIVOT, this element will be
appended to greater side, otherwise to lower side


                             -Source code
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers.pop()

    greater_items = []
    lower_items = []
    for item in numbers:
        if item > pivot:
           greater_items.append(item)
        else:
            lower_items.append(item)

    return quick_sort(lower_items) + [pivot] + quick_sort(greater_items)


print(quick_sort([3, 7, 1, 6, 2, 4]))

###########################################################################################


5) MERGE SORT

                            -Theory
Usually done recursively
 It works on the principle of Divide and Conquer
repeatedly breaks down a list into several
sublists until each sublist consists of a single element


                            -Source code
def merge_sort(numbers):
    if len(numbers) > 1:
        left_numbers = numbers[:len(numbers) // 2]
        right_numbers = numbers[len(numbers) // 2:]

        # Recursion
        merge_sort(left_numbers)
        merge_sort(right_numbers)

        # Merge
        i = 0     # left_numbers   index
        j = 0     # right_numbers  index
        k = 0     # merged numbers index

        while i < len(left_numbers) and j < len(right_numbers):
            if left_numbers[i] < right_numbers[j]:
                numbers[k] = left_numbers[i]
                i += 1
            else:
                numbers[k] = right_numbers[j]
                j += 1
            k += 1

        while i < len(left_numbers):
            numbers[k] = left_numbers[i]
            i += 1
            k += 1

        while j < len(right_numbers):
            numbers[k] = right_numbers[j]
            j += 1
            k += 1


test_nums = [5, 2, 7, 4, 1, 3, 6, 8]
merge_sort(test_nums)
print(test_nums)

################################################################################


6) HEAP SORT

                            -Theory
Heapsort is a comparison based sorting technique based on a Binary
Heap data structure. It is similar to selection sort where we
first find the maximum element and place the maximum element
at the end. We repeat the same process for the remaining element.


                        -Source code
def swap(my_list, i, j):
    my_list[i], my_list[j] = my_list[j], my_list[i]


def sift_down(my_list, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if my_list[i] >= max(my_list[l], my_list[r]):
                break
            elif my_list[l] > my_list[r]:
                swap(my_list, i, l)
                i = l
            else:
                swap(my_list, i, r)
                i = r

        elif l < upper:
            if my_list[l] > my_list[i]:
                swap(my_list, i, l)
                i = l
            else:
                break

        elif r < upper:
            if my_list[r] > my_list[i]:
                swap(my_list, i, r)
                i = r
            else:
                break

        else:
            break


def heap_sort(my_list):
    for j in range((len(my_list) - 2) // 2, -1, -1):
        sift_down(my_list, j, len(my_list))

    for end in range(len(my_list) -1, 0, -1):
        swap(my_list, 0, end)
        sift_down(my_list, 0, end)


my_list = [4, 7, 2, 9, 1, 0, 10]
heap_sort(my_list)
print(my_list)


##########################################################


7) RADIX SORT


                        -Theory
This algorithm is efficient if we already know the range
of target values. The time complexity of the algorithm
is O(nk) O ( n k ) . n is the size of the input list and k
is the digit length of the number. For example, The digit
length of 512 is 3.


                        -Source code
def counting_sort(number, place):
    size = len(number)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = number[i] // place
        count[index % 10] += 1
    for j in range(1, 10):
        count[j] += count[j - 1]

    k = size - 1
    while k >= 0:
        index = number[k] // place
        output[count[index % 10] - 1] = number[k]
        count[index % 10] -= 1
        k -= 1
    for a in range(0, size):
        number[a] = output[a]


def radix_sort(number):
    max_num = max(number)
    place = 1
    while max_num // place > 0:
        counting_sort(number, place)
        place *= 10


number_1 = [106, 104, 52, 72, 201]
radix_sort(number_1)
print(number_1)


