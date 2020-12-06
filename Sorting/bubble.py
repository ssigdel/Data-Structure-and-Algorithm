def bubble_sort(data):
    for i in range(0, len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
            print(i,j, data)
    return data

if __name__ == "__main__":
    data = [4, 3, 5, 7, 1]
    print(bubble_sort(data))


