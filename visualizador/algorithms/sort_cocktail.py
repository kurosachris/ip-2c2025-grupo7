def cocktail_sort(arr):
    swapped = True
    start = 0
    end = len(arr) - 1

    while swapped:
        swapped = False

        # Loop from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If nothing moved, then the array is sorted
        if not swapped:
            break

        swapped = False

        # Move the end point back by one, as the last element is in place
        end -= 1

        # Loop from right to left
        for i in range(end, start - 1, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Move the starting point forward, as the first element is in place
        start += 1

    return arr

# Example usage:
if __name__ == '__main__':
    sample_list = [5, 3, 8, 4, 2]
    sorted_list = cocktail_sort(sample_list)
    print("Sorted list:", sorted_list)