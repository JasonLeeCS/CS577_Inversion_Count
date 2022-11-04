#
# Inversion Count
# Assignment: HW 5 CS577
# Author: Jason Lee (jlee967@wisc.edu)
#
#
def mergeCount(arr1, arr2):
    merge, count, i, j = [], 0, 0, 0
    l, r = len(arr1), len(arr2)

    # merge sort
    while i < l and j < r:
        # if merging from right array count++
        if arr2[j] < arr1[i]:
            merge.append(arr2[j])
            count += l - i
            j += 1
        else:
            merge.append(arr1[i])
            i += 1

    # add remaining elements
    if i == l:
        merge.extend(arr2[j:])
    elif j == r:
        merge.extend(arr1[i:])

    return merge, count

def inversion(n, arr):
    # base case
    if n == 1:
        return (arr, 0)

    # split array in half
    middle = n // 2
    front = arr[:middle]
    back = arr[middle:]

    # recursive calls
    A, countA = inversion(middle, front)
    B, countB = inversion(n - middle, back)

    C, countC = mergeCount(A, B)
    total = countA + countB + countC

    return C, total


def main():
    instance = int(input())

    result = ""
    for _ in range(instance):
        n = int(input())  # array length

        arr = [int(i) for i in input().split()]

        _, count = inversion(n, arr)
        result += f"{count}\n"

    return result.rstrip() 


if __name__ == "__main__":
    print(main())