def main():
    TAX_RATE = 20

    gross_pay = get_gross_pay()
    net_pay = get_net_pay(gross_pay, TAX_RATE)

    print(f"Gross Pay: {gross_pay:.2f}")
    print(f"Net Pay: {net_pay:.2f}")    


def get_net_pay(gross_pay, tax_rate):
    return gross_pay - (gross_pay * tax_rate / 100)

def get_gross_pay():
    while True:
        radius = input("Enter the gross pay: ")

        if radius.isdigit():
            return float(radius)
        
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()