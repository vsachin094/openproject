def calculate_tax(income, nps_percentage=0, basic_salary_percentage=50):
    # Standard deduction of ₹75,000
    standard_deduction = 75000
    basic_salary = income * (basic_salary_percentage / 100)  # Basic salary is 50% of income
    nps_investment = basic_salary * (nps_percentage / 100)  # NPS as % of Basic Salary

    taxable_income = max(0, income - standard_deduction - nps_investment)

    # Updated tax slabs (New Regime 2024-25)
    tax_slabs = [
        (400000, 0.00),  # Up to ₹4,00,000 - 0%
        (800000, 0.05),  # ₹4,00,001 - ₹8,00,000 - 5%
        (1200000, 0.10), # ₹8,00,001 - ₹12,00,000 - 10%
        (1600000, 0.15), # ₹12,00,001 - ₹16,00,000 - 15%
        (2000000, 0.20), # ₹16,00,001 - ₹20,00,000 - 20%
        (2400000, 0.25), # ₹20,00,001 - ₹24,00,000 - 25%
        (float('inf'), 0.30) # Above ₹24,00,000 - 30%
    ]

    tax = 0
    prev_limit = 0

    for limit, rate in tax_slabs:
        if taxable_income > prev_limit:
            taxable_amount = min(taxable_income, limit) - prev_limit
            tax += taxable_amount * rate
            prev_limit = limit
        else:
            break

    # Apply rebate under Section 87A if taxable income ≤ ₹12,75,000
    if taxable_income <= 1275000:
        tax = 0  

    # Apply Health and Education Cess (4% of tax)
    cess = tax * 0.04
    total_tax = tax + cess

    return total_tax, nps_investment, taxable_income

# Example usage
income = float(input("Enter your annual income (in ₹): "))
nps_percentage = float(input("Enter NPS investment percentage of Basic Salary (in %): "))
basic_salary_percentage = 50  # Basic salary is 50% of total income

tax, nps_investment, taxable_income = calculate_tax(income, nps_percentage, basic_salary_percentage)

print(f"Your NPS investment: ₹{nps_investment:,.2f}")
print(f"Your taxable income after deductions: ₹{taxable_income:,.2f}")
print(f"Your total income tax payable: ₹{tax:,.2f}")