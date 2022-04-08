def quicksort(arr: list):
    def qsort(arr: list, left: int, right: int):
        if left < right:
            k = (left + right) // 2
            v = arr[k]
            i, j = left, right
            while i < j:
                while i < right and arr[i] <= v:
                    i += 1
                while j > left and arr[j] > v:
                    j -= 1

                if i < j and arr[i] > arr[j]:
                    # pivot gets swapped, remember new pos
                    if k == i: k = j
                    if k == j: k = i
                    arr[i], arr[j] = arr[j], arr[i]

            arr[j], arr[k] = arr[k], arr[j]

            qsort(arr, left, j - 1, )
            qsort(arr, j + 1, right)

    qsort(arr, 0, len(arr) - 1)


# This one may crash when list size are big.
# Because in worst case, the time complexity is O(n^2),
# the recursive call will make stack overflow.
def quicksort1(arr: list):
    def qsort(left: int, right: int, arr: list):
        if left < right:
            # choose pivot in the middle will be error
            # k = (left + right) // 2
            k = left 
            v = arr[k]
            i, j = left, right
            while i < j:
                while i < right and arr[i] <= v:
                    i += 1
                while j > left and arr[j] > v:
                    j -= 1

                if i < j and arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

            arr[j], arr[k] = arr[k], arr[j]

            qsort(left, j - 1, arr)
            qsort(j + 1, right, arr)

    qsort(0, len(arr) - 1, arr)


if __name__ == '__main__':
    nums = [3, 7, 7, 4, 8, 5, 4, 6, 8, -4, 4, -6, 9, 0, 1]
    quicksort(nums)
    print(nums)
    assert(nums == [-6, -4, 0, 1, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 9])
