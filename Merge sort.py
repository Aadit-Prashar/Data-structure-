def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2   # find middle
        left_half = arr[:mid]      # left half
        right_half = arr[mid:]     # right half

        # recursive call
        left_sorted=merge_sort(left_half)
        right_sorted=merge_sort(right_half)

        i = j = k = 0

        # merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # check for remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)