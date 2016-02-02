__author__ = 'The Forge'
import random,time

def inplace_quick_sort(list):
    inplace_quick_sort_range(list, 0, len(list))
    return list

def inplace_quick_sort_range(list, start, end):
    if (end-start) > 1:
        lt_end, gt_start = inplace_partition(list, start, end)
        inplace_quick_sort_range(list, start, lt_end)
        inplace_quick_sort_range(list, gt_start, end)

def inplace_partition(list, start, end):
    pivot = list[random.randint(start, end-1)]

    # first pass: partition list into LT, GE zones
    lt_end = start
    ge_start = end

    while lt_end < ge_start:
        if list[lt_end] < pivot:
            lt_end += 1
        elif list[ge_start-1] >= pivot:
            ge_start -= 1
        else:
            swap(list, lt_end, ge_start-1)

    # second pass: partition GE into EQ, GT zones
    eq_end = lt_end
    gt_start = end
    while eq_end < gt_start:
        if list[eq_end] == pivot:
            eq_end +=1
        elif list[gt_start-1] > pivot:
            gt_start -= 1
        else:
            swap(list, eq_end, gt_start-1)
            eq_end += 1
    return lt_end, gt_start

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def to_read(source):

    # open file
    source = open('beowulf.txt', 'r')

    # read the contents and split it into words
    content = source.read().split()

    # close file
    source.close()

    # First 10 words
    my_lines = []

    for line in range(0, 10):
        my_lines.append(content[line])

    return my_lines

def user_input():
    get_input = input("requested n: ")
    print(get_input)

def main():
    source = ""
    user_input()
    content = to_read(source)

    print("Unsorted: ", content)
    print("In-place Sorting...")
    start = time.perf_counter()
    inplace_quick_sort(content)
    end = time.perf_counter()
    print("  Sorted: ", content)
    print('Elapsed time = ' + str(end - start) + 'seconds')

if __name__ == "__main__":
    main()