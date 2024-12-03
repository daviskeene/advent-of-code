def is_safe(arr):
    # Check if this array is "safe"
    # Either all increasing or all decreasing
    # Any two adjacent numbers differ by at least one and at most 3

    first_diff = arr[1] - arr[0]
    sign = 1 if first_diff >= 0 else -1

    # First edge case
    if abs(first_diff) < 1 or abs(first_diff) > 3:
        return False

    for i in range(1, len(arr) - 1):
        elem1 = arr[i]
        elem2 = arr[i + 1]
        diff = elem2 - elem1
        # Check if increasing/decreasing
        if diff >= 0 and sign == -1 or diff < 0 and sign == 1:
            return False
        # Check if > 1 or <= 3
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    # Always increasing/decreasing, adjacent elements never
    # differ by less than 1 or more than 3
    return True

def lossy_shuffle(arr):
    # Returns len(arr) arrays with one element removed from each
    # e.g. lossy_shuffle([1,2,3]) -> [[2,3], [1,3], [1,2]]
    arrs = []
    for i in range(len(arr)):
        new_arr = arr[0:i] + arr[(i + 1):len(arr)]
        arrs.append(new_arr)
    return arrs

def is_safe_with_dampener(arr):
    # Check if this array is "safe"
    # if any one of the elements are removed
    potentially_safe_arrs = lossy_shuffle(arr)
    for array in potentially_safe_arrs:
        if is_safe(array):
            return True
    return False


if __name__ == "__main__":
    # Read input
    with open('./input/day2_input.txt') as file:
        lines = file.readlines()
        safe_lines = 0
        safe_with_dampener_lines = 0
        for line in lines:
            arr = [int(x) for x in line.split(" ")]
            if is_safe(arr):
               safe_lines += 1
            if is_safe_with_dampener(arr):
                safe_with_dampener_lines += 1
        print(safe_lines) 
        print(safe_with_dampener_lines)