def main():
    number = get_number()

    if number <= 10:
        print("The number belongs to the range 0-10.")
    elif number <= 20:
        print("The number belongs to the range 11-20.")
    elif number <= 30:
        print("The number belongs to the range 21-30.")
    elif number <= 40:
        print("The number belongs to the range 31-40.")


def get_number():
    while True:
        number = input("Enter a number from 0 to 40: ")

        try:
            number = float(number)

            if number < 0 or number > 40:
                raise ValueError("Number out of range.")
            
            return number
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()