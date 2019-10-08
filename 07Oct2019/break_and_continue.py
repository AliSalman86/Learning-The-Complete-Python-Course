# break is to stop the loop when a condition met
cars = ["ok", "ok", "ok", "faulty", "ok", "ok", "faulty"]
count = 0
for status in cars:
    if status == "faulty":
        # using break
        # print("Stopping the production line!")
        # break
        # stop the loop completely
        # using continue instead will jump back to the begining of the loop skipping
        # the false element
        print("Found faulty car, skipping...")
        continue
    count += 1
    print("====================================================")
    print(f"This car is {status}")
    print(f"Shipping new car to the customer")
    print(f"number of units shipped is {count}")
    print("====================================================")
