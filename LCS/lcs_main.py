from lcs import length_lcs
from lcs import lcs

if __name__ == "__main__":
    x = list(input("\n Enter the first sequence:"))
    y = list(input("\n Enter the second sequence:"))
    m = len(x)
    n = len(y)
    (array, length) = length_lcs(x, y, m, n)
    print('\n Length of lcs is:', length)
    print('\n LCS is:', lcs(x, y, array, length))