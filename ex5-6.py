try:
    # Read inputs
    gross = float(input("Enter gross salary: "))
    children = int(input("Enter number of children: "))

    # Determine base tax rate
    if gross < 1000:
        tax_rate = 0.10
    elif gross < 2000:
        tax_rate = 0.12
    elif gross < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    # Apply reduction based on children
    if gross < 2000:
        tax_rate -= children * 0.01
    else:
        tax_rate -= children * 0.005

    # Avoid negative tax
    if tax_rate < 0:
        tax_rate = 0

    # Compute net salary
    net = gross * (1 - tax_rate)

    print("Net salary:", net)

except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter numbers only.")