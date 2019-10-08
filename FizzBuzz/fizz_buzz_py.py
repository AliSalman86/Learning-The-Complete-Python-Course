# The famous FizzBuzz
# iterate over range of numbers from 1 and 100 both inclusive using for loop
for number in range(1,101):
    # if the number can be divided by 3 and 5 then FizzBuzz
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    # if the number can be divided by 3 then Fizz
    elif number%3 == 0:
        print("Fizz")
    # if the number can be divided by 5 then Buzz
    elif number%5 == 0:
        print("Buzz")
    # just print the number
    else:
        print(number)
