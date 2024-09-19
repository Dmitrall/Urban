numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes_ = []

for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            #break
    if not is_prime:
        not_primes_.append(number)
    else:
        primes_.append(number)
print ('primes:', primes_)
print ('not primes:', not_primes_)