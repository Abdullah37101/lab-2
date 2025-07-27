from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        return datetime.now() - self.date_of_birth

def main():
    person = Person(
        name="Abdullah",
        country="Egypt",
        date_of_birth=datetime(2010, 7, 7)
    )

    print(f"Age: {person.age().days // 365} years")


if __name__ == "__main__":
    main()