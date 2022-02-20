# Problem for Prof Charnesky's mid term review sheet at:
# https://canvas.umd.umich.edu/courses/522665/pages/midterm-practice?module_item_id=9243802
# 1 question on recursion
# Write a recursive function(s) sum_of_ordinal_values_in_string( some_string ) that returns the sum of the ordinal
# values of all of the characters.
# Write an iterative function sum_of_ordinal_values_in_string( some_string ) that returns the sum of the ordinal
# values of all of the characters.

def sum_of_ordinal_values_in_string_iterative(some_string):
    total = 0
    for i in range(0, len(some_string)):
        total += ord(some_string[i])
    print(total)


def count_rep(some_string, rep):
    if rep < 2:
        return ord(some_string[rep - 1])
    return ord(some_string[rep - 1]) + count_rep(some_string, rep - 1)


def sum_of_ordinal_values_in_string_recursion(some_string):
    rep = len(some_string)
    print(count_rep(some_string, rep))


if __name__ == "__main__":
    some_string = "总"
    print("now we try:", some_string)
    print("iterative answer is: ")
    sum_of_ordinal_values_in_string_iterative(some_string)
    print("recursive answer is: ")
    sum_of_ordinal_values_in_string_recursion(some_string)

