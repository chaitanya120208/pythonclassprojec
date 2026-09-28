#  Cafe Bill Calculator

A simple Python console program that calculates a cafe bill for six fixed menu items, including item-wise **18% GST** and a **grand total**.

##  Description

This program asks the user for the price and quantity of each item on a small, fixed menu. It then calculates the cost of each item, applies 18% GST to every item individually, and prints a neatly formatted, itemized bill showing each item's total, its GST, the overall subtotal, the total GST, and the final grand total.

##  Menu Items

| Item | GST Rate |
|---|---|
| Pizza | 18% |
| Burger | 18% |
| Chocolate Ice Cream | 18% |
| French Fries | 18% |
| Sandwich | 18% |
| Smoothie | 18% |

##  Features

- Takes price and quantity as input for each of the 6 menu items
- Calculates the total cost per item (`price × quantity`)
- Calculates 18% GST on **each item individually**
- Computes the subtotal (before GST), total GST, and grand total
- Prints a clean, itemized bill to the console

##  Requirements

- Python 3.x (no external libraries needed)

##  How to Run

1. Save the script as `cafe_bill.py`
2. Open a terminal in the same folder
3. Run:
   ```bash
   python cafe_bill.py
   ```
4. Enter the price and quantity for each item when prompted

##  How It Works (Code Structure)

1. **Input** – `input()` collects the price (`float`) and quantity (`int`) for each of the 6 items.
2. **Item totals** – Each item's total is calculated as `price * quantity`.
3. **Subtotal** – `total_before_gst` is the sum of all item totals.
4. **GST calculation** – Each item's GST is calculated separately as `item_total * 18 / 100`, then summed into `total_gst`.
5. **Grand total** – `grand_total = total_before_gst + total_gst`.
6. **Output** – All totals are printed as a formatted bill.
