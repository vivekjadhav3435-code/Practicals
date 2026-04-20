import math
number = int(input("Enter a number: "))
if (1<= number <=9): # Single-digit number
    print(number**2)
elif (9 < number <= 99): # Twodigit number 6
    print(f"{math.sqrt(number):.2f}")
elif (100 <= number <= 999): # Threedigit number | 
    print(f"{math.cbrt(number):.2f}")
else:
    print("Invalid")