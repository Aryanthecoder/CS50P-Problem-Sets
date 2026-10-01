def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False

    seen_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            if i > 0 and s[i - 1].isdigit() is False and char == "0":
                return False  
            seen_digit = True
        elif seen_digit:
            return False

    return True

if __name__ == "__main__":
    main()
