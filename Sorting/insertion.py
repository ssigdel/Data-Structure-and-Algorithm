import random

def insertion(data):
    for i in range(1, len(data)):
        key = data[i]

        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = key


if __name__ == "__main__":
    data = random.sample(range(0, 10), 10)
    print(data)
    insertion(data)
    print(data)
