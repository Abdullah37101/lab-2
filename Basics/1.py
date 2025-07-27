def main():
    length = get_length()
    cm = to_cm(length)
    print(f"The length in centimeters is: {cm:.2f}")


def to_cm(inches):
    return inches * 2.54

def get_length():
    while True:
        radius = input("Enter the length in inches: ").strip()

        try:
            return float(radius)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()