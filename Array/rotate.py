import random

# rotate arr elements left to right
def rotate(arr, n):
    temp = arr [n - 1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i -1]
    arr[0] = temp
    return arr

#driver function
if __name__ == '__main__':
    arr = random.sample(range(0, 10), 10)
    #number of values to rotate
    d = 3   
    n = len(arr)
    arr.sort()
    for j in range(d):
        print(rotate(arr, n))