# Problem for Prof Charnesky's mid term review sheet at:
# https://canvas.umd.umich.edu/courses/522665/pages/midterm-practice?module_item_id=9243802
# 1 2d list question
# Write a function sum_of_values_in_even_product_of_indexes( some_list ) that returns the sum of all values in
# indexes whose product of row and column index is even.

def sum_of_values_in_even_product_of_indexes(some_list):
    total = 0
    row = 0
    column = 0
    for row in range(len(some_list)):
        for column in range(len(some_list[row])):
            if row * column % 2 == 0:
                total += some_list[row][column]
    print(total)


if __name__ == "__main__":
    some_list = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [1, 2, 1, 2]
    ]
    sum_of_values_in_even_product_of_indexes(some_list)
