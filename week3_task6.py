products = int(input("Enter number of products: "))
total_price = float(input("Enter total price: "))

discount = 0

if total_price > 1000 and products > 3:
    discount = 0.15
elif total_price > 500:
    discount = 0.10

discount_amount = total_price * discount
final_bill = total_price - discount_amount

print("Discount Applied:", discount * 100, "%")
print("Final Bill:", final_bill)
