import euclidean_algorithm as ea


def relatively_primes(a, b):
    euclidean_result = ea.euclidean_algorithm(a, b)
    ea.euclidean_list_display(euclidean_result)
    if euclidean_result[-1][2] == 1:
        print("Numbers are relatively prime.")
    else:
        print("Numbers are not relatively prime.")


if __name__ ==  "__main__":
    a = ea.user_input()
    b = ea.user_input()

    relatively_primes(a, b)
