def main():
    NUMBER_OF_NUMBERS = 5
    numbers = get_numbers(NUMBER_OF_NUMBERS)

    print(get_evens(numbers))


def get_evens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)

    return evens

def get_numbers(number_of_numbers):
    numbers = []
    for _ in range(number_of_numbers):
        number = get_number()
        numbers.append(number)

    return numbers

def get_number():
    while True:
        number = input("Enter a number to add: ").strip()

        try:
            return int(number)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()