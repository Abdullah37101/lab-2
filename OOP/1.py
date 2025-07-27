class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius


def main():
    circle = Circle(get_radius())
    
    print(f"Area of the circle: {circle.area()}")
    print(f"Circumference of the circle: {circle.circumference()}")

def get_radius():
    while True:
        number = input("Enter the radius: ").strip()

        try:
            return int(number)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()