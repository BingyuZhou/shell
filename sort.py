#!/usr/bin/env python

import numpy as np

"""
time profiling (line profiler): 
```
kernprof -l -v sort.py
```

memory profiling:

```
python -m memory_profiler sort.py
```

"""


@profile
def insert_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp
            j -= 1


@profile
def quick_sort(arr, i, j):
    if i >= j:
        return

    pivot = arr[j]

    left = i
    right = j - 1

    while left <= right:
        if arr[left] < pivot:
            left += 1
        elif arr[right] > pivot:
            right -= 1
        elif arr[left] >= pivot and arr[right] <= pivot:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
            left += 1
            right -= 1

    tmp = arr[left]
    arr[left] = pivot
    arr[j] = tmp

    quick_sort(arr, i, left - 1)
    quick_sort(arr, left + 1, j)


def main():
    arr = np.random.randint(0, 100, 100)
    arr_copy = arr
    insert_sort(arr_copy)
    print(arr_copy)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    main()
