#implementation of lcs for given sequence of elements
#takes two sequence as input
#return array and its length
def length_lcs(x, y, m, n):
    arr = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif x[i -1] == y[j -1]:
                arr[i][j] = arr[i -1][j -1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    return arr, arr[m][n]

#takes sequence, array and its length as input
# returns lcs 
def lcs(x, y, array, length):
    current_index = length
    lcs = ["" for i in range(current_index)]
    i = len(x)
    j = len(y)
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            lcs[current_index -1] = x[i -1]
            i -= 1
            j -= 1
            current_index -= 1

        elif array[i-1][j] > array[i][j-1]:
            i-= 1
        else:
            j -= 1
    return lcs







