def main():
    
    s = get_string()
    
    if is_palindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")


def get_string():
    while True:
        s = input("Enter a string: ").strip()
        
        if s:
            return s

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
        
    return True


if __name__ == "__main__":
    main()