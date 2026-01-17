# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

def average_valid_measurements(values):
    if not values:
        return None
    total = 0
    count = 0
    for v in values:
        if v is not None:
            if isinstance(v, (int, float)) and not isinstance(v, bool):#Ignores None and non-numeric values.
                total += v
                count += 1
    
    return total / count if count > 0 else 0

