def calculate_monthly_salary(ctc):
    """
    Calculate monthly in-hand salary after deductions using a loop.

    Args:
        ctc (float): Annual Cost to Company (CTC).

    Returns:
        dict: Contains hra, da, pf, annual tax, monthly in-hand salary.
    """
    deductions = {
        "HRA": 0.10,  # HRA is 10% of CTC
        "DA": 0.05,   # DA is 5% of CTC
        "PF": 0.03    # PF is 3% of CTC
    }

    results = {}

    # Calculate HRA, DA, and PF using a loop
    for key, percentage in deductions.items():
        results[key] = ctc * percentage

    # Determine tax rate based on CTC slabs
    tax_rate = 0
    if 5_00_000 < ctc <= 7_50_000:
        tax_rate = 0.5
    elif ctc > 7_50_000:
        tax_rate = 0.10
    elif ctc > 15_00_000:
        tax_rate = 0.15

    results["Annual Tax"] = ctc * tax_rate

    # Calculate total deductions
    total_deductions = sum(results.values())

    # Calculate monthly in-hand salary
    annual_inhand_salary = ctc - total_deductions
    results["Monthly In-hand Salary"] = annual_inhand_salary/12
    results["Yearly  In-hand Salary"] = annual_inhand_salary


    return results

# Example usage
ctc = float(input("Enter your annual CTC: "))
result = calculate_monthly_salary(ctc)

print("\nSalary Breakdown:")
for key, value in result.items():
    print(f"{key}: {value:,.2f}")
