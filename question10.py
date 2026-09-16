def check_number(num):
    if num < 2:
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        return "Prime"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))

print(check_number(num))
