#Grocery Bill Calculator
items = []
price = []

n = int(input("Enter the number of items: "))
totalCost = 0

print("---- Receipt: ----")
for i in range(1, n+1):
    ite = input(f"Enter the item {i}: ")
    items.append(ite)
    pri = float(input(f"Enter the price of item {i}: "))
    price.append(pri)
    totalCost += pri
    
print("==============================")
for i in range(n):
    print("{:<20} {:>10.2f}".format(items[i], price[i]))
print("==============================")
print(f"Total Cost: {totalCost}")
print("==============================")

#Shopping Discount 
discount_perc = float(input("Enter discount percentage: "))
disc_amount = (discount_perc/100)*totalCost
print("==============================")
print(f"Discount Amount: {disc_amount}")
print(f"Final cost: {totalCost-disc_amount}")
print("==============================")
print("Thank you for shopping with us!")