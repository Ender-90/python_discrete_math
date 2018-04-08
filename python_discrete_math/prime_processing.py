def looking_for_prime(n, list_of_primes):
    ls = list_of_primes
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    if is_prime:
        ls.append(n)

    return ls


def next_primes(n, list_of_primes):
    ls_in = list(list_of_primes)
    ls_out = list(list_of_primes)
    counter = 0
    i = list_of_primes[-1] + 1

    while counter < n:
        ls_out = looking_for_prime(i, ls_out)
        if len(ls_out) > len(ls_in):
            counter += 1
            ls_in = list(ls_out)

        i += 1

    return ls_out


def primes_in_range(n, list_of_primes):
    ls = list_of_primes

    for i in range(1, n):
        ls = looking_for_prime(i, ls)

    return ls


def display_list_of_primes(list_of_primes):
    width = 0
    while list_of_primes[-1] % (10 ** width) != list_of_primes[-1]:
        width += 1

    for i in range(len(list_of_primes)):
        print("{0:{1}} ".format(list_of_primes[i], width), end ='')
        if (i + 1) % 36 == 0 or i == len(list_of_primes) - 1:
            print("")


if __name__ == "__main__":
    list_pr = []
    list_pr = primes_in_range(2000, list_pr)

    display_list_of_primes(list_pr)
    list_pr = next_primes(1000, list_pr)
    display_list_of_primes(list_pr)



    # filename = "prime_list.txt"
    # file = open(filename, 'a')
    # for i in range(len(list_pr)):
    #     file.write(str(list_pr[i]) + "\n")
    #
    # file.close()