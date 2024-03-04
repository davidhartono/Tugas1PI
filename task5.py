numbers = []
while True:
    number = int(input("Enter a number (-1 to stop): "))
    if number == -1:
        break
    numbers.append(number)
total = sum(numbers)
print(total)
