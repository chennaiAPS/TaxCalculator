def calculate_old_regime(income, deductions):
    taxable_income = income - deductions

    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (taxable_income - 1000000) * 0.3

    return tax


def calculate_new_regime(income):
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = (300000 * 0.05) + (income - 600000) * 0.1
    elif income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (300000 * 0.15) + (income - 1200000) * 0.2
    else:
        tax = (300000 * 0.05) + (300000 * 0.1) + (300000 * 0.15) + (300000 * 0.2) + (income - 1500000) * 0.3

    return tax


# User Input
income = float(input("Enter your annual income: "))
regime = input("Choose regime (old/new): ").lower()

if regime == "old":
    deductions = float(input("Enter total deductions: "))
    tax = calculate_old_regime(income, deductions)
else:
    tax = calculate_new_regime(income)

print(f"Your total tax is: ₹{tax}")