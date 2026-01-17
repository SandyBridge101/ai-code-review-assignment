# Notes (Optional)

## Assumptions Made

### Task 1 - Average Order Value
- Assumed that returning `0` for edge cases (empty list, all cancelled orders) is acceptable. Alternative approaches could return `None` to distinguish "no data" from "zero average", or raise a `ValueError` with a descriptive message.
- Assumed all order dictionaries contain both "status" and "amount" keys. In production, would add validation to handle missing keys gracefully.
- Assumed "cancelled" is the only invalid status. If there are other statuses to exclude ("pending", "failed"), the function would need modification.

### Task 2 - Count Valid Emails
- Used a standard email regex patterns for common cases, but does **not** support:
  - Quoted strings in local part (e.g., `"john doe"@example.com`)
  - Comments (e.g., `john.doe(comment)@example.com`)
  - IP addresses as domains (e.g., `user@[192.168.1.1]`)
  - Internationalized domain names (IDN) with unicode characters
- Assumed that emails with leading/trailing whitespace should be accepted after stripping. If strict validation is required, these could be rejected.
- The regex requires TLD to be at least 2 characters, which excludes some valid but rare single-character TLDs.

### Task 3 - Aggregate Valid Measurements
- Assumed that boolean values (True/False) should **not** be treated as measurements, even though they're technically numeric in Python. This is a judgment call - in some contexts, booleans might be valid (e.g., binary sensor data).
- Chose to return `None` for empty input and `0` for all-invalid input to distinguish these cases. Alternative: return `None` for both, or raise exceptions.
- Assumed standard Python numeric types (int, float) are sufficient. Did not handle `Decimal`, `Fraction`, or numpy numeric types.

## Known Limitations

### Task 1
- No input validation: assumes `orders` is a list of dictionaries with correct structure
- No handling of negative amounts (which might indicate refunds)
- No handling of zero amounts (which might be valid for free orders or should be filtered)

### Task 2
- The regex pattern is a practical compromise, not RFC 5322 compliant for all edge cases
- No actual domain validation (doesn't check if domain exists or has MX records)
- International email addresses with non-ASCII characters are not supported
- Does not validate local part length limits (64 chars) or total email length (254 chars)

### Task 3
- No handling of `math.inf`, `math.nan`, or infinity values - these would pass type checking but could corrupt the average
- No overflow protection for very large sums
- No precision handling for floating-point arithmetic edge cases


## General Testing Philosophy

For all three tasks, I focused testing considerations on:
1. **Happy path**: Normal expected inputs
2. **Edge cases**: Empty, single-item, boundary conditions
3. **Error conditions**: Invalid types, malformed data, None values
4. **Business logic**: Cancelled orders, invalid emails, mixed types

In a real production environment, I would:
- Write comprehensive unit tests using pytest
- Add property-based tests using hypothesis for edge case discovery
- Include integration tests with realistic datasets
- Add performance benchmarks for large inputs
- Document expected behavior in docstrings with examples
