import time

print("Celsius-Fahrenheit Program!")
time.sleep(2)

n = None
while n is None: 
    try:
        n = float(input("Enter the temperature: "))
    except ValueError: 
        print("Invalid Number")

unit = input("What do you want to convert this to? (F/C) ").lower()

if unit == "f":
    result = n * 1.8 + 32
    print(str(result) + " F")
elif unit == "c":
    result = (n - 32) * 5/9
    print(str(result) + " C")
else: 
    print("Invalid Input!")
