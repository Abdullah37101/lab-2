def main():
    NUMBER_OF_NUMBERS = 5
    numbers = get_numbers(NUMBER_OF_NUMBERS)

    while True:
        order = get_order()

        if order > len(numbers):
            print("Order exceeds the number of elements in the list. Please try again.")
        
        break

    print(largest(numbers, order))


def largest(numbers, order):
    if order > len(numbers):
        raise ValueError("Order exceeds the number of elements in the list.")
    
    sorted_numbers = sorted(numbers)

    return sorted_numbers[-order]

def get_order():
    while True:
        order = input("Enter the order of the largest number to find: ").strip()

        try:
            order = int(order)
            if order <= 0:
                raise ValueError("Order must be a positive integer.")
            
            return order
        
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

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