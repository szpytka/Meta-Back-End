def calculate_tax(bill, tax_rate):
    return round(((bill * tax_rate) / 100.00), 2)


print(f"Total tax: {calculate_tax(175, 15)}")
print(f"Total tax: {calculate_tax(164.33, 22)}")
