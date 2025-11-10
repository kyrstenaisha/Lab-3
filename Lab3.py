print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # REQ-04: If 0 numbers → return 0
    if len(arr) == 0:
        return 0

    # REQ-03: If >= 10 numbers → return 1
    if len(arr) >= 10:
        return 1

    # REQ-05: Check if non-integer → return 2
    for x in arr:
        if not isinstance(x, int):
            return 2

    # Safe copy
    arr_result = arr.copy()
    n = len(arr_result)

    # REQ-01 / REQ-02 — Perform bubble sort
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    # Return the sorted list according to sorting order
    return arr_result


def main():
    # Example driver
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort ascending
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort descending
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)


if __name__ == "__main__":
    main()
