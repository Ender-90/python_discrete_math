def euclidean_algorithm(n, m):
    if n == 0 or m == 0:
        print("Numbers have not be equal to 0!")
    start_a = m
    start_b = n

    if start_b < 1:
        start_b *= -1

    if start_a < 1:
        start_a *= -1

    result_list = None
    if start_a > start_b:
        result_list = [[start_a, start_a // start_b, start_b, start_a % start_b]]
    else:
        result_list = [[start_b, start_b // start_a, start_a, start_b % start_a]]

    while result_list[-1][2] != 1 and result_list[-1][3] != 0:
        a = result_list[-1][2]
        b = result_list[-1][3]
        c = result_list[-1][2] % result_list[-1][3]
        result_list.append([a, a // b, b, c])

    return result_list


def user_input():
    while True:
        try:
            int_input = int(input("Input a number: "))
            return int_input
        except ValueError:
            print("Please input an integer!")


a = user_input()
b = user_input()
list_to_display = euclidean_algorithm(a, b)
print(list_to_display)
