def calculate_discount(price, discount):
    
    if discount >= 20:
        return price * (1 - discount / 100)
    else:
        return price


print("Welcome to the Discount Calculator!")
print("----------------------------------")


product_name = input("What product are you purchasing? ")
original_price = float(input(f"Enter the original price of {product_name}: "))
discount_percent = float(input(f"Enter the discount percentage for {product_name}: "))


final_price = calculate_discount(original_price, discount_percent)

# result 
print("\n--- Receipt ---")
print(f"Product: {product_name}")
if discount_percent >= 20:
    print(f"Original price: ${original_price:.2f}")
    print(f"Discount applied: {discount_percent}%")
    print(f"Final price: ${final_price:.2f}")
else:
    print(f"No discount applied (needed 20% or higher)")
    print(f"Price: ${original_price:.2f}")

print("\nThank you for using our calculator!")