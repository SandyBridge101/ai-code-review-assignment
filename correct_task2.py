# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re

def count_valid_emails(emails):
    # Handle None or empty input
    if not emails:
        return 0
    
    #Regular expression pattern for a valid email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    count = 0
    
    for email in emails:
        # Skip non-string items safely
        if not isinstance(email, str):
            continue
            
        # Strip whitespace and validate
        email = email.strip()
        
        if email and re.match(email_pattern, email):
            count += 1
    
    return count