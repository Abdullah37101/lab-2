def main():
    NUMBER_OF_NUMBERS = 1
    numbers = get_numbers(NUMBER_OF_NUMBERS)

    if is_palindrome(numbers):
        print("The list is a palindrome.")
    else:
        print("The list is not a palindrome.")


def is_palindrome(numbers):
    for i in range(len(numbers) // 2):
        if numbers[i] != numbers[-(i + 1)]:
            return False
        
    return True

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