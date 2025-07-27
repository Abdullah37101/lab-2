def main():
    number = get_number()
    print(f"The square of {number} is {square_number(number)}")


def square_number(num):    
    return num * num

def get_number():
    while True:
        number = input("Enter a number to square: ").strip()

        try:
            return float(number)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()