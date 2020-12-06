#unittest case for testing
import unittest
import random

#merge_sort implementation function. divides the arr into
#left and right and pass to merge function
def merge_sort(arr):
    size = len(arr)
    if size == 1:
        return
    else:
        mid = size // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
    
        merge(left, right, arr)

#takes left and right array list, sorts them and stores value in array
def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

if __name__ == '__main__':
    arr = random.sample(range(0, 10), 10)
    print(arr)
    merge_sort(arr)
    print(arr)
    unittest.main()
    
#unit test implementation for merge sort 
class Test_merge_sort(unittest.TestCase):
    def test_merge_sort(self):
        data = [1, 4, 5, 3, 2]
        print(data)
        merge_sort(data)
        sorted_arr = [1, 2, 3, 4, 5]
        print(sorted_arr)
        self.assertListEqual(data, sorted_arr)


    