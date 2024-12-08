try:
    value_total = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percent_cal = value / value_total * 100
    print(f"That is: {percent_cal}%")
except ValueError:
    print("You need to enter a number. Run the program again")

except ZeroDivisionError:
    print("Your total value cannot be zero.")