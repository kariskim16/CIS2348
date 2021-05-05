"""
Karis Kim
1624226
CIS 2348
"""
def selection_sort_descend_trace(lst):
    for n in range(len(lst) - 1):
        largest_value = n
        for j in range(n + 1, len(lst)):
            if lst[j] > lst[largest_value]:
                largest_value = j
        lst[n], lst[largest_value] = lst[largest_value], lst[n]
        for i in lst:
            print(i, end=' ')
        print()
    return lst
if __name__ == '__main__':
    numbers = [int(i) for i in input().split()]
    selection_sort_descend_trace(numbers)
