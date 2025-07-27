from math import pi

def main():
    radius = get_radius()
    volume = get_volume(radius)
    print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")


def get_volume(radius):
    return 4 / 3 * pi * radius ** 3

def get_radius():
    while True:
        radius = input("Enter the radius: ")

        try:
            return float(radius)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()