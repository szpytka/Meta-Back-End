bill_total = 210;
discount_one = 10;
discount_two = 20;

if bill_total > 100 and bill_total < 200:
  print("Bill is greater than 100!")
  bill_total = bill_total - discount_one
elif bill_total > 200:
  print("Bill is greater than 200!")
  bill_total = bill_total - discount_two
else:
  print("Bill is less than 100.")

print(f"Total bill: {bill_total}")