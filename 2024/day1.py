from collections import Counter

def solve_1(a_arr, b_arr):
    """
    Two sorted columnar lists of data. Compare the adjacent elements, get the difference.
    Return the sum of the differences.
    """
    diffs = 0

    for i in range(len(a_arr)):
        diff = abs(a_arr[i] - b_arr[i])
        diffs += diff
    
    return diffs

def solve_2(a_arr, b_arr):
    """
    Two sorted columnar lists of data. For each value in A, count how many times it appears in B.
    Multiply the number of B occurences by this value. Repeat until solved.
    """
    result = 0
    # Trick: only need to count occurences in B, then check if
    # the counter keys contain the element from A (0 otherwise)
    b_count = Counter(b_arr)
    for i in range(len(a_arr)):
        num = a_arr[i]
        # Count number of times this number is in B
        occurences = b_count[num] or 0
        result += occurences * num
    return result

if __name__ == "__main__":
    # Spaces between values in day1_input.txt
    delimeter = "   "
    with open("./day1_input.txt") as f:
        lines = f.readlines()
        a_arr = []
        b_arr = []
        for line in lines:
            a, b = line.strip().split(delimeter)
            a_arr.append(int(a))
            b_arr.append(int(b))
        # Sort arrays (in place)
        a_arr.sort()
        b_arr.sort()
        # day1 part1
        print(solve_1(a_arr, b_arr))
        # day1 part2
        print(solve_2(a_arr, b_arr))