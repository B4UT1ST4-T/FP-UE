Import re

while True:
    try:
       age = int(input("Please enter your age: "))
       if 0 <= age <= 120:
        print("Thank you for providing your age.")
        break
    except ValueError:
        print("Enter a valid age inside the range (0-120)")
