# recives the number to calculate the sum of all its divisors
from typing import List

initial_number = int(input("Please enter a integer number: ").strip())


# factorization into primes
factors = []
potential_prime = 2
while initial_number > 1:
    if initial_number % potential_prime == 0:
        initial_number = round(initial_number / potential_prime)
        factors.append(potential_prime)
    else:
        potential_prime += 1

# splits the prime factor and its frequency into two different lists
a = -1
frequency: List[int]  = []
primefactors: List[int]  = []
for i in factors:
    if i in primefactors:
        frequency[a] += 1
    else:
        frequency.append(0)
        a += 1
        frequency[a] += 1
        primefactors.append(i)

# just make the sum of all its div
final_sum = 1
for k in range(len(primefactors)):
    a = primefactors[k]
    b = frequency[k]
    final_sum *= ((a ** (b + 1)) - 1) / (a - 1)

print("The sum of all divisors is: ",int(final_sum))
