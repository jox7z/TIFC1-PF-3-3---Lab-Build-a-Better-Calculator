
def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total

def isiteven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def isitaninteger(num):
    if isinstance(num, int):
        return True
    else:
        return False

def main():
    print(addmultiplenumbers([5, 7, 9]))
    print(multiplymultiplenumbers([5, 7, 9]))
    print(isiteven(4))
    print(isitaninteger(5))

if __name__ == "__main__":
    main()