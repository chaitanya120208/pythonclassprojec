# cafe bill calculator 
pizza_price = float(input("Enter the price of pizza: "))
pizza_quantity = int(input("Enter the quantity of pizza: "))
burger_price = float(input("Enter the price of burger: "))
burger_quantity = int(input("Enter the quantity of burger: "))
chocolateicecream_price = float(input("Enter the price of chocolate ice cream: "))
chocolateicecream_quantity = int(input("Enter the quantity of chocolate ice cream: "))
french_fries_price = float(input("Enter the price of french fries: "))
french_fries_quantity = int(input("Enter the quantity of french fries: "))
sandwich_price = float(input("Enter the price of sandwich: "))
sandwich_quantity = int(input("Enter the quantity of sandwich: "))
smoothie_price = float(input("Enter the price of smoothie: "))
smoothie_quantity = int(input("Enter the quantity of smoothie: "))

# Calculate item totals 
pizza_total = pizza_price * pizza_quantity
burger_total = burger_price * burger_quantity
chocolateicecream_total = chocolateicecream_price * chocolateicecream_quantity
french_fries_total = french_fries_price * french_fries_quantity
sandwich_total = sandwich_price * sandwich_quantity
smoothie_total = smoothie_price * smoothie_quantity

# total before gst 
total_before_gst = pizza_total + burger_total + chocolateicecream_total + french_fries_total + sandwich_total + smoothie_total

# gst calculation
pizza_gst = pizza_total*18/100  # 18% GST
burger_gst = burger_total*18/100  # 18% GST
chocolateicecream_gst = chocolateicecream_total*18/100  # 18% GST
french_fries_gst = french_fries_total*18/100  # 18% GST
sandwich_gst = sandwich_total*18/100  # 18% GST
smoothie_gst = smoothie_total*18/100  # 18% GST

total_gst = pizza_gst + burger_gst + chocolateicecream_gst + french_fries_gst + sandwich_gst + smoothie_gst

#grand total
grand_total = total_before_gst + total_gst

print("\n----- CAFE BILL -----")
print("pizza total   : Rs.", pizza_total)
print("burger total  : Rs.", burger_total)
print("chocolate ice cream total: Rs.", chocolateicecream_total)
print("french fries total: Rs.", french_fries_total)
print("sandwich total: Rs.", sandwich_total)
print("smoothie total: Rs.", smoothie_total)

print("----------------------")
print("Total   :",total_before_gst)
print("Pizza GST (18%):",pizza_gst)
print("Burger GST (18%):",burger_gst)
print("Chocolate Ice Cream GST (18%):",chocolateicecream_gst)
print("French Fries GST (18%):",french_fries_gst)
print("Sandwich GST (18%):",sandwich_gst)
print("Smoothie GST (18%):",smoothie_gst)
print("total GST: Rs.", total_gst)
print("----------------------")

print("grand total: Rs.", grand_total)
