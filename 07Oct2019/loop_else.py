# else keyword used with loops would run the block of code it has if the for or while
# loop didn't encounter a break during iteration as shown in below code
cars = ["ok", "ok", "ok", "ok", "ok", "ok", "ok"]
count = 0
for status in cars:
    if status == "faulty":
        # using break
        print("Stopping the production line!")
        break
        # stop the loop completely
        # using continue instead will jump back to the begining of the loop skipping
        # the false element
        # print("Found faulty car, skipping...")
        # continue
    count += 1
    print("====================================================")
    print(f"This car is {status}")
    print(f"Shipping new car to the customer")
    print(f"number of units shipped is {count}")
    print("====================================================")
# code for else keyword will run only if no break occured, all cars are OK
# doesn't work with continue!!!
else:
    print("All cars are ok, no faulty cars")
