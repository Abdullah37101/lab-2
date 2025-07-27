def main():
    input_string = get_string()
    
    print(input_string[::-1])


def get_string():
    while True:
        s = input("Enter a string: ").strip()
        
        if s:
            return s

if __name__ == "__main__":
    main()