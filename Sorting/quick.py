import random

def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    
def partition(data, low, high):
    pivot = data[high]
    i = (low - 1)
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            swap(data, i, j)
    swap(data, i+1, high)
    return (i+1)

def quickSort(data, low, high):
    if low < high:
        pi = partition(data, low, high)
        quickSort(data, low, pi-1)
        quickSort(data, pi + 1, high)

if __name__ == "__main__":
    data = random.sample(range(0, 10), 10)
    print(data)
    low = 0
    high = len(data)-1
    quickSort(data, low, high)
    print(data)
