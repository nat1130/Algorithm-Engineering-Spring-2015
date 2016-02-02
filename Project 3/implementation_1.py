__author__ = 'The Forge'
import time

def in_place_selection_sort(list):

    #answer = input('Amount of words: ')
    #print('Will do', answer, 'of work')

    for k in range(len(list)-1):
        least = k
        for i in range(k+1, len(list)):
            if list[i] < list[least]:
                least = i
        list[k], list[least] = list[least], list[k]
    return list

def to_read(source):

    # open file
    source = open('beowulf.txt', 'r')

    # read the contents and split it into words
    content = source.read().split()

    # close file
    source.close()

    # First 10 words
    my_lines = []
    answer = input('Enter the amount of words you want to do: ')
    print("About to do work for", answer, "words")
    num_words = int(answer)
    for line in range(0, num_words):
        my_lines.append(content[line])

    return my_lines

def main():
    source = ""
    content = to_read(source)

    print("Unsorted: ")
    for i in range(0,10):
        print(content[i])
    print("=======================")
    print("In-place Sorting...")
    print("=======================")
    start = time.perf_counter()
    in_place_selection_sort(content)
    end = time.perf_counter()
    print("Sorted:")
    for i in range(0,10):
        print(content[i])
    print('Elapsed time = ' + str(end - start) + 'seconds')

if __name__ == "__main__":
    main()
