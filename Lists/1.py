def main():
    NUMBER_OF_NUMBERS = 5
    numbers = get_numbers(NUMBER_OF_NUMBERS)

    unique_numbers = set(numbers)
    print(list(unique_numbers))


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