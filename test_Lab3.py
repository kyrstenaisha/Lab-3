from Lab3 import bubble_sort, SORT_ASCENDING, SORT_DESCENDING

def test_sort_ascending():
    assert bubble_sort([3,1,2], SORT_ASCENDING) == [1,2,3]

def test_sort_descending():
    assert bubble_sort([3,1,2], SORT_DESCENDING) == [3,2,1]

def test_too_many_numbers():
    assert bubble_sort([1,2,3,4,5,6,7,8,9,10], SORT_ASCENDING) == 1

def test_no_numbers():
    assert bubble_sort([], SORT_ASCENDING) == 0

def test_non_integer():
    assert bubble_sort([1,"a",3], SORT_ASCENDING) == 2
