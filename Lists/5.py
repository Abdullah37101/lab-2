def main():
    NUMBER_OF_ITEMS = 10
    items = get_numbers(NUMBER_OF_ITEMS)

    print(f"Your shopping list items are: {items}")
    print(f"Second item in the list: {items[1]}")
    print(f"Eighth item in the list: {items[7]}")


def get_numbers(number_of_numbers):
    numbers = []
    for _ in range(number_of_numbers):
        number = get_number()
        numbers.append(number)

    return numbers

def get_number():
    while True:
        number = input("Enter a shopping list item to add: ").strip()

        if number:
            return number
        
        print("Please enter a valid item.")


if __name__ == "__main__":
    main()