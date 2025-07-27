def main():
    a = get_number()
    b = get_number()

    print(f"The largest number is: {largest(a, b)}")


def largest(a, b):
    if a > b:
        return a
    
    return b

def get_number():
    while True:
        number = input("Enter a number: ").strip()

        try:
            return float(number)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()