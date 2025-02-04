def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: A single element is already sorted

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two halves while comparing elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add remaining elements (if any)
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Test Merge Sort
arr = [5, 2, 4, 7, 1, 3, 2, 6]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
