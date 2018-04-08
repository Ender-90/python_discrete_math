def input_positive_integer():
    while True:
        try:
            int_input = int(input("Input a number: "))
            if int_input > 0:
                return int_input
                break
            else:
                print("Please input a positive integer!")
        except ValueError:
            print("Please input a positive integer!")


def prime_factors(int_to_factors):
    width = 1
    while int_to_factors % (10 ** width) != int_to_factors:
        width += 1
    factor_rest = int_to_factors
    while factor_rest != 1:
        divisor = 2
        for i in range(2, factor_rest + 1):
            if factor_rest % i == 0:
                divisor = i
                break
        print("{0:{1}} | {2}".format(factor_rest, width, divisor))
        factor_rest //= divisor
    print("{0:{1}} |". format(1, width))


if __name__ == "__main__":    
    user_input = input_positive_integer()
    print("")
    prime_factors(user_input)
