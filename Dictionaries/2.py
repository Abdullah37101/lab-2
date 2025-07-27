def main():
    dictionary = {
        "test": "c",
        "example": "a",
        "sample": "b",
    }

    key = get_key()
    if key in dictionary:
        print(f"Key '{key}' found with value: {dictionary[key]}")
    else:
        print(f"Key '{key}' not found in the dictionary.")


def get_key():
    while True:
        key = input("Enter a key to search: ")
        
        if key:
            return key
        

if __name__ == "__main__":
    main()