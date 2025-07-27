def main():
    dictionary = {
        "test": "c",
        "example": "a",
        "sample": "b",
    }

    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    print("Original Dictionary:", dictionary)
    print("Sorted Dictionary:", sorted_dict)


if __name__ == "__main__":
    main()