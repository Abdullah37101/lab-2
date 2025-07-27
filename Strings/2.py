def main():
    input_string = get_string()

    upper_letters, lower_letters = count_case(input_string)
    
    print(f"No. of Upper case characters : {upper_letters}")
    print(f"No. of Lower case characters : {lower_letters}")


def get_string():
    while True:
        s = input("Enter a string: ").strip()
        
        if s:
            return s

def count_case(s):
    upper_letters = 0
    lower_letters = 0

    for char in s:
        if char.isupper():
            upper_letters += 1
        elif char.islower():
            lower_letters += 1

    return upper_letters, lower_letters


if __name__ == "__main__":
    main()