temp = int(input("What temp do you want to convert? > "))
temp_unit = input("Is that C or F? > ").lower()
answer = ''
if temp_unit == "c":
    answer = (9 / 5) * temp + 32
elif temp_unit == "f":
    answer = 5 / 9 * (temp - 32)
else:
    answer = "Invalid input"
print(f"{temp}{temp_unit} equals {answer}")
