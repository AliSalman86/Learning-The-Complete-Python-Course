# prime numbers are numbers divided by itself and 1
# list to store the primes
primes = list()
count = 0
# first we will iterate through the range we want to find the primes within
# starting from 2 as all numbers given to be divided by 1, and 2 is first prime number
for number in range(2,1001):
# nested loop to check the number checker range (2 to the number)
    for checker in range(2,number):
# iterate the number over all the checkers
# if the number divisive by any checker, the number is not a prime
        if number % checker == 0:
# break and continue in nested loops affect only the nearest loop
            break
# if number is not divisive by any checker then it's prime
# No break occured for the loop then the number can be appended to the primes list
# as else block
    else:
        count += 1
        primes.append(number)
# print the list
print(primes)
print(f"There are {count} prime numbers between 2 and 1000")
