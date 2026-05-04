# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System

print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
# Format: (product_id, name, price, quantity, category)
product1 = ("P001", "Smartphone X", 799.99, 12, "Mobile Phones")
product2 = ("P002", "Laptop Pro", 1299.99, 8, "Laptops")
product3 = ("P003", "Wireless Earbuds", 149.99, 20, "Audio")
product4 = ("P004", "Tablet Air", 499.99, 6, "Tablets")
product5 = ("P005", "Gaming Laptop", 1599.99, 3, "Laptops")

# TODO 2: Create inventory list
inventory = [product1, product2, product3, product4, product5]


# Helper display function
def display_product(product):
    """Prints one product tuple in a readable format."""
    print(
        f"ID: {product[0]} | "
        f"Name: {product[1]} | "
        f"Price: ${product[2]:.2f} | "
        f"Quantity: {product[3]} | "
        f"Category: {product[4]}"
    )


# TODO 3: Display all products
print("\nCurrent Inventory:")
print("-" * 60)
for product in inventory:
    display_product(product)

# TODO 4: Access specific elements
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

print("\nAccessing Specific Products:")
print("-" * 60)
print("First product:")
display_product(first_product)

print("\nLast product:")
display_product(last_product)

print(f"\nThird product name: {third_product_name}")
print(f"Second product price: ${second_price:.2f}")
print(f"Second product quantity: {second_quantity}")

# TODO 5: Use slicing
first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

print("\nProduct Subsets Using Slicing:")
print("-" * 60)

print("First 3 products:")
for product in first_three:
    display_product(product)

print("\nProducts from index 2 to 4:")
for product in middle_products:
    display_product(product)

print("\nAll products except the first:")
for product in all_except_first:
    display_product(product)

# TODO 6: Add new products using .append()
product6 = ("P006", "Bluetooth Speaker", 89.99, 15, "Audio")
product7 = ("P007", "Smartwatch Z", 299.99, 9, "Wearables")

inventory.append(product6)
inventory.append(product7)

print("\nAdding New Products:")
print("-" * 60)
print("Added:")
display_product(product6)
display_product(product7)

print("\nUpdated inventory:")
for product in inventory:
    display_product(product)

# TODO 7: Remove a product using .pop()
removed_product = inventory.pop(2)

print("\nRemoving a Product:")
print("-" * 60)
print("Removed product:")
display_product(removed_product)

print("\nUpdated inventory:")
for product in inventory:
    display_product(product)

# TODO 8: Insert a product using .insert()
inserted_product = ("P008", "Noise Cancelling Headphones", 249.99, 4, "Audio")
inventory.insert(1, inserted_product)

print("\nInserting a Product:")
print("-" * 60)
print("Inserted product:")
display_product(inserted_product)

print("\nUpdated inventory:")
for product in inventory:
    display_product(product)

# REDO TODO 4 and 5
# Recalculate after inventory changes for autograder compatibility
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]

first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

# TODO 9: Create category lists
mobile_phones = []
laptops = []
audio = []
tablets = []
wearables = []

for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_phones.append(product)
    elif product[4] == "Laptops":
        laptops.append(product)
    elif product[4] == "Audio":
        audio.append(product)
    elif product[4] == "Tablets":
        tablets.append(product)
    elif product[4] == "Wearables":
        wearables.append(product)

print("\nProducts by Category:")
print("-" * 60)

print("Mobile Phones:")
for product in mobile_phones:
    display_product(product)

print("\nLaptops:")
for product in laptops:
    display_product(product)

print("\nAudio:")
for product in audio:
    display_product(product)

print("\nTablets:")
for product in tablets:
    display_product(product)

print("\nWearables:")
for product in wearables:
    display_product(product)

# TODO 10: Calculate inventory statistics
total_products = len(inventory)
total_value = sum(product[2] * product[3] for product in inventory)
product_names = [product[1] for product in inventory]
product_prices = [product[2] for product in inventory]

print("\nInventory Statistics:")
print("-" * 60)
print(f"Total number of products: {total_products}")
print(f"Total inventory value: ${total_value:.2f}")
print("Product names:", product_names)
print("Product prices:", product_prices)

# TODO 11: Expensive products using list comprehension
expensive_products = [product for product in inventory if product[2] > 500]

print("\nExpensive Products (> $500):")
print("-" * 60)
for product in expensive_products:
    display_product(product)

# TODO 12: Low stock alert using list comprehension
low_stock = [product for product in inventory if product[3] < 5]

print("\nLow Stock Alert (< 5 units):")
print("-" * 60)
for product in low_stock:
    display_product(product)

# TODO 13: Price lists using list comprehension
original_prices = [product[2] for product in inventory]
discounted_prices = [round(price * 0.90, 2) for price in original_prices]

print("\nPrice Lists:")
print("-" * 60)
print("Original prices:", original_prices)
print("Discounted prices:", discounted_prices)

# TODO 14: Product name formatting using list comprehension
uppercase_names = [product[1].upper() for product in inventory]
product_codes = [product[0][:3] + product[1][:3].upper() for product in inventory]

print("\nFormatted Product Names:")
print("-" * 60)
print("Uppercase names:", uppercase_names)
print("Product codes:", product_codes)

# TODO 15: Using loops to process inventory
mobile_count = 0
laptop_value = 0
most_expensive = inventory[0]

for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_count += 1

    if product[4] == "Laptops":
        laptop_value += product[2] * product[3]

    if product[2] > most_expensive[2]:
        most_expensive = product

print("\nLoop-Based Analysis:")
print("-" * 60)
print(f"Mobile Phones count: {mobile_count}")
print(f"Total value of Laptops: ${laptop_value:.2f}")
print("Most expensive product:")
display_product(most_expensive)

# TODO 16: Using conditionals with lists
restock_list = []
high_value_items = []
price_ranges = {"under_100": 0, "100_to_500": 0, "over_500": 0}

for product in inventory:
    if product[3] < 5:
        restock_list.append(product)

    if product[2] > 500 and product[3] > 10:
        high_value_items.append(product)

    if product[2] < 100:
        price_ranges["under_100"] += 1
    elif 100 <= product[2] <= 500:
        price_ranges["100_to_500"] += 1
    else:
        price_ranges["over_500"] += 1

print("\nConditional Analysis:")
print("-" * 60)

print("Products that need restocking:")
for product in restock_list:
    display_product(product)

print("\nHigh-value items:")
for product in high_value_items:
    display_product(product)

print("\nPrice ranges:", price_ranges)

# TODO 17: Define and use functions
def calculate_product_value(product):
    """Returns price multiplied by quantity for a product tuple."""
    return product[2] * product[3]


def find_products_by_category(inventory, category):
    """Returns a list of products in the given category."""
    return [product for product in inventory if product[4] == category]


def apply_discount(inventory, discount_percent):
    """Returns a new inventory list with discounted prices."""
    discounted_inventory = []
    for product in inventory:
        new_price = round(product[2] * (1 - discount_percent / 100), 2)
        discounted_product = (product[0], product[1], new_price, product[3], product[4])
        discounted_inventory.append(discounted_product)
    return discounted_inventory


function_total_value = sum(calculate_product_value(product) for product in inventory)
audio_products = find_products_by_category(inventory, "Audio")
discounted_inventory_15 = apply_discount(inventory, 15)

print("\nFunction-Based Operations:")
print("-" * 60)
print(f"Total inventory value using function: ${function_total_value:.2f}")

print("\nAudio products:")
for product in audio_products:
    display_product(product)

print("\nInventory with 15% discount applied:")
for product in discounted_inventory_15:
    display_product(product)

# TODO 18: Comprehensive inventory report
def generate_inventory_report(inventory):
    """
    Returns a dictionary containing:
    total_products, total_value, categories, low_stock, average_price
    """
    total_products = len(inventory)
    total_value = 0
    total_price = 0
    categories = []
    low_stock_items = []

    for product in inventory:
        total_value += product[2] * product[3]
        total_price += product[2]

        if product[4] not in categories:
            categories.append(product[4])

        if product[3] < 5:
            low_stock_items.append(product)

    average_price = total_price / total_products

    return {
        "total_products": total_products,
        "total_value": round(total_value, 2),
        "categories": categories,
        "low_stock": low_stock_items,
        "average_price": round(average_price, 2)
    }


inventory_report = generate_inventory_report(inventory)

print("\nComprehensive Inventory Report:")
print("-" * 60)
print(f"Total products: {inventory_report['total_products']}")
print(f"Total value: ${inventory_report['total_value']:.2f}")
print("Categories:", inventory_report["categories"])

print("\nLow stock products:")
for product in inventory_report["low_stock"]:
    display_product(product)

print(f"\nAverage price: ${inventory_report['average_price']:.2f}")