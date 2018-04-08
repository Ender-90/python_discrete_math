from math import gcd
import prime_factoring as pf


def phi(a):
    counter = 0

    for k in range(1, a + 1):
        if gcd(a, k) == 1:
            counter += 1

    return counter


def fast_phi(a):
    prime_list = pf.prime_factors_to_list(a)
    result = 1
    for i in range(1,len(prime_list)):
        result *= (prime_list[i][0] ** (prime_list[i][1] - 1)) * (prime_list[i][0] - 1)
    return result


if __name__ == "__main__":
    # print(fast_phi(98))
    # print(fast_phi(99))
    # print(phi(8))
    # print(phi(27))
    # print(fast_phi(27))
    # print(phi(100))
    # print(fast_phi(100))
    # print(phi(23554325))
    # print(fast_phi(23554325))
    # print(fast_phi(45784789887457))
    user_input = pf.input_positive_integer()

    print("Result of calculating Euler's totient function (faster mode):  {}".format(fast_phi(user_input)))
    print("Result of calculating Euler's totient function (slower mode):  {}".format(phi(user_input)))
