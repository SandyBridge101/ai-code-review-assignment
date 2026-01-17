# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    if not orders:
        return 0
    
    total = 0
    count = len(orders)

    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]
        
    return total / count if count > 0 else 0