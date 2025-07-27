def main():
    length = get_temperature()
    fahrenheit = to_fahrenheit(length)
    print(f"The temperatue in fahrenheit is: {fahrenheit:.2f}")


def to_fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def get_temperature():
    while True:
        radius = input("Enter the temperate in celsius: ")

        if radius.isdigit():
            return float(radius)
        
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()