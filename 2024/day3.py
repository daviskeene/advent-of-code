# # #
#  no regex challenge
# # #

def parse_lines_for_mul(line: str):
    # part 1
    mul_sum = 0
    # From each line (string), find instances of a mul(a,b)
    # and perform that calculation, summing the results
    potential_args = line.split("mul(")

    for arg in potential_args:
        # the first part of the string is our contender for the argument
        first_num, *rest = arg.split(',')
        # second number is going to be whatever follows
        second_num = next(iter(next(iter(rest), '').split(')')), None)
        try:
            first_num = int(first_num)
            second_num = int(second_num)
        except ValueError:
            # can't multiply non-numbers
            continue
        mul_sum += first_num * second_num
    return mul_sum

def parse_lines_for_mul_do_dont(line: str, is_do = True):
    # part 2
    # From each line (string), find instances of a mul(a,b)
    # that _do not_ follow a don't() instruction
    # perform that calculation, summing the results

    # heuristic: get substrings after a do(), before a don't()
    # first substring: if not is_do, exclude it
    ans = sum(list(map(lambda x: parse_lines_for_mul(x.split("don't()")[0]), line.split("do()")[(0 if is_do else 1) : ])))
    # Determine whether or not our line has ended on do() or don't()
    # to pass to the next iteration
    # (this would have been so much easier if I just made this all one string for the input)
    # (oh well)
    new_is_do = line.rfind('do()') > line.rfind("don't()")
    return ans, new_is_do

if __name__ == "__main__":
    with open('./input/day3_input.txt') as file:
        lines = file.readlines()

        part1_sum = 0
        part2_sum = 0

        # keeps track of whether or not multiplication is
        # enabled for the next iteration of part 2's solution
        is_do = True
        # iterate over file lines
        for line in lines:
            mul_sum = parse_lines_for_mul(line)
            mul_sum_2, new_is_do = parse_lines_for_mul_do_dont(line, is_do)

            part1_sum += mul_sum
            part2_sum += mul_sum_2

            is_do = new_is_do
        print(part1_sum)
        print(part2_sum)