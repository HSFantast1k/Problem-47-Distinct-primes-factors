def is_prime(number):
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True


number = 0
prime_number = [num for num in range(1, 10000) if is_prime(num) and num % 2 != 0]
not_prime_number = [num for num in range(1, 10000) if not is_prime(num) and num % 2 != 0]
list = []


for not_prime in not_prime_number:
    low_num_prime = [num for num in range(1, 10000) if is_prime(num) and num < not_prime]
    low_num_prime = low_num_prime[::-1]
    for num_prime in low_num_prime:
        i = 1
        Flag = False
        while not_prime >= num_prime + 2 * i ** 2 and not_prime not in list:
            if not_prime == num_prime + 2 * i ** 2:
                print("{0} ------ {1} ------ {2}".format(not_prime, num_prime, i))
                list.append(not_prime)
                Flag = True
                break
            i += 1
        if Flag:
           break
print(set(not_prime_number) - set(list))
input()