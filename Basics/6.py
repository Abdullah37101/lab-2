def main():
    while True:
        number = get_number()
        if number < 0:
            return

def get_number():
    while True:
        number = input("Enter a number: ")

        try:
            return float(number)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()