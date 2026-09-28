# ☕ Cafe Bill Calculator

A simple Python console program that calculates a cafe bill for six fixed menu items, including item-wise **18% GST** and a **grand total**.

## 📋 Description

This program asks the user for the price and quantity of each item on a small, fixed menu. It then calculates the cost of each item, applies 18% GST to every item individually, and prints a neatly formatted, itemized bill showing each item's total, its GST, the overall subtotal, the total GST, and the final grand total.

## 🍕 Menu Items

| Item | GST Rate |
|---|---|
| Pizza | 18% |
| Burger | 18% |
| Chocolate Ice Cream | 18% |
| French Fries | 18% |
| Sandwich | 18% |
| Smoothie | 18% |

## ✨ Features

- Takes price and quantity as input for each of the 6 menu items
- Calculates the total cost per item (`price × quantity`)
- Calculates 18% GST on **each item individually**
- Computes the subtotal (before GST), total GST, and grand total
- Prints a clean, itemized bill to the console

## 🛠️ Requirements

- Python 3.x (no external libraries needed)

## ▶️ How to Run

1. Save the script as `cafe_bill.py`
2. Open a terminal in the same folder
3. Run:
   ```bash
   python cafe_bill.py
   ```
4. Enter the price and quantity for each item when prompted

## 💻 Sample Run

**Input:**
```
Enter the price of pizza: 250
Enter the quantity of pizza: 2
Enter the price of burger: 180
Enter the quantity of burger: 1
Enter the price of chocolate ice cream: 120
Enter the quantity of chocolate ice cream: 2
Enter the price of french fries: 90
Enter the quantity of french fries: 1
Enter the price of sandwich: 150
Enter the quantity of sandwich: 1
Enter the price of smoothie: 110
Enter the quantity of smoothie: 1
```

**Output:**
```
----- CAFE BILL -----
pizza total   : Rs. 500.0
burger total  : Rs. 180.0
chocolate ice cream total: Rs. 240.0
french fries total: Rs. 90.0
sandwich total: Rs. 150.0
smoothie total: Rs. 110.0
----------------------
Total   : 1270.0
Pizza GST (18%): 90.0
Burger GST (18%): 32.4
Chocolate Ice Cream GST (18%): 43.2
French Fries GST (18%): 16.2
Sandwich GST (18%): 27.0
Smoothie GST (18%): 19.8
total GST: Rs. 228.60000000000002
----------------------
grand total: Rs. 1498.6
```

## 🧠 How It Works (Code Structure)

1. **Input** – `input()` collects the price (`float`) and quantity (`int`) for each of the 6 items.
2. **Item totals** – Each item's total is calculated as `price * quantity`.
3. **Subtotal** – `total_before_gst` is the sum of all item totals.
4. **GST calculation** – Each item's GST is calculated separately as `item_total * 18 / 100`, then summed into `total_gst`.
5. **Grand total** – `grand_total = total_before_gst + total_gst`.
6. **Output** – All totals are printed as a formatted bill.

## ⚠️ Known Limitations

- The menu is **hardcoded** to exactly 6 items — it can't handle a different number of items or a custom menu without editing the code.
- There is **no input validation**, so entering text or a negative number will crash the program or produce an incorrect bill.
- GST amounts are floating-point numbers, so results like `228.60000000000002` can appear due to standard floating-point rounding — this is a Python/IEEE‑754 quirk, not a calculation error.
- Every item uses the same fixed 18% GST rate; there's no support for items with different tax slabs.

## 🚀 Possible Future Improvements

- Store the menu in a **dictionary** so items can be added/removed easily
- Use a **loop** to support any number of items instead of repeating code per item
- Add **input validation** (reject negative prices/quantities, handle non-numeric input)
- Round final amounts to 2 decimal places for cleaner currency output
- Add support for **discounts** or multiple GST slabs
- Save each bill to a file or export it as a PDF receipt

## 📄 License

This project is free to use and modify for learning purposes.
