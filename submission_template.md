# AI Code Review Assignment (Python)

## Candidate
- Name: Tariq Nasser Deen
- Approximate time spent: 70 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Division by zero error: When the orders list is empty, count = len(orders) returns 0, causing ZeroDivisionError on the final division.


### Edge cases & risks
- Empty orders list causes crash
- Missing "status" or "amount" keys in order dictionaries would cause KeyError

### Code quality / design issues
- Variable naming is clear and follows conventions

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added check for empty input to return 0 early
- Added safety check if count > 0 before division to handle all-cancelled scenario

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty list: Ensure it returns 0 without crashing

- All cancelled orders: Verify it returns 0

- Mixed cancelled/valid orders: Confirm average excludes cancelled orders

- No cancelled orders: Ensure standard averaging works correctly

- Single order (cancelled and non-cancelled): Edge case for count = 1

- Malformed data: Test with missing keys, invalid types to ensure graceful handling or clear error messages

- Large datasets: Performance testing with thousands of orders

- Floating point amounts: Verify precision with decimal values


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Says it divides by "number of orders" which is ambiguous—doesn't clarify it should be non-cancelled orders only

- Doesn't mention what happens with empty input or all-cancelled scenarios

- The explanation masks the critical division by zero issue

### Rewritten explanation
- This function calculates the average order value for non-cancelled orders only. It iterates through the orders list, summing the amounts of orders where status is not "cancelled". The average is computed by dividing the total by the count of orders. If the input is empty or all orders are cancelled, the function returns 0 to avoid division by zero and indicate no valid orders to average.

## 4) Final Judgment
- Decision: Approve

- Justification: The function properly addresses the critical division by zero bug by adding checks for empty input and all-cancelled scenarios. The logic for summing amounts and counting valid orders is sound, and the variable naming is clear. The function now behaves correctly across all identified edge cases.

- Confidence & unknowns: High confidence in the bugs identified. The fixes are straightforward and well-tested patterns. Unknown is around whether 0 is the appropriate return value for edge cases, or if None or raising an exception would be better.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Grossly oversimplified validation: Only checks if "@" exists in the string, which accepts invalid emails like "@@", "@domain", "user@", "not an email @ all"

- No format validation: Missing checks for proper email structure (local part, domain, TLD)

- Type error risk: If the emails list contains non-string items, the function might fail with TypeError

### Edge cases & risks
- None or empty input list not handled.

- Whitespace-only strings or strings with spaces would pass validation.

- Empty strings would fail validation but are not explicitly handled.

- Leading/trailing whitespace in otherwise valid emails would be counted, but the whitespace itself makes them technically invalid.

- Multiple "@" symbols would pass validation.

- Missing domain would pass validation.


### Code quality / design issues
- No use of proper validation patterns (regex)
- No input sanitization
- Function could be more robust with explicit validation rules

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added proper email regex pattern: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
- Added None/empty input handling to return 0 early
- Added type checking to skip non-string items safely
- Added strip() to remove leading/trailing whitespace before validation
- Added check for empty string after stripping

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Valid standard emails
- Valid edge cases: Single character local/domain (a@b.co), numbers, hyphens, underscores
- Invalid - missing sections
- Invalid - formatting
- Invalid - special chars
- Empty/whitespace
- Whitespace handling
- Mixed case(should be valid)
- Non-string inputs
- Empty list and None input: Boundary conditions

Why?
- Email validation is security-sensitive
- False positives could allow spam or invalid data into the system
- False negatives could reject legitimate users
- Type errors could crash the application

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The original code does NOT safely ignore invalid entries, it accepts almost anything with an "@" symbol
- Original code doesn't handle None or empty list, it would crash or behave unexpectedly
- Doesn't explain what makes an email valid

### Rewritten explanation
- This function counts valid email addresses using regex pattern matching to ensure proper email structure. A valid email must contain a local part (alphanumeric characters with allowed special characters like dots, underscores, plus signs), followed by "@", a domain name, and a top-level domain of at least 2 characters. The function handles edge cases including None/empty input (returns 0), non-string items in the list (skipped), and whitespace around emails (stripped before validation). Empty strings after stripping are rejected. The validation is strict but follows common email format standards.

## 4) Final Judgment
- Decision: Approve

- Justification: Implements proper email validation with regex, handles all edge cases (None input, empty list, non-string items, whitespace), and uses appropriate type checking.

- Confidence & unknowns: Very high confidence. The core logic is correct and comprehensive. Unknown: Specific requirements around email validation strictness (internationalization, quoted strings).

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- float(v) will raise ValueError or TypeError when v is a non-numeric type
- Python's isinstance(v, int) returns True for booleans since bool is a subclass of int. The original code would treat True as 1.0 and False as 0.0, polluting the average
- If all values are None or invalid, count = len(values) causes division by zero
- Uses len(values) instead of counting only valid measurements, giving incorrect average

### Edge cases & risks
- Empty list causes division by zero
- List with all None values: division by zero
- Mixed types will lead to type conversion crashes
- List with single valid value should return that value
- Negative numbers should be allowed for measurements

### Code quality / design issues
- No input validation or type checking before conversion
- Assumes all non-None values are numeric
- Return type inconsistency potential

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added empty input check to return None early
- Replaced ```len(values)``` with a counter that only increments for valid measurements
- Added explicit type checking: isinstance(v, (int, float)) before processing
- Added explicit boolean exclusion: and not isinstance(v, bool) to prevent treating True/False as numbers
- Changed division to use count of valid values instead of len(values)
- Added safety check if count > 0 before division, returns 0 if no valid measurements
- Removed unsafe direct conversion of ```float(v)```

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- All valid numbers: [1, 2, 3, 4, 5] 
- Mixed with None: [1, None, 3, None, 5]
- All None: [None, None, None] → should return 0
- Empty list: []
- Single value: [42]
- Mixed types: [1, "2", 3, [4], {"five": 5}]
- Booleans: [1, True, 2, False, 3]
- Floats and integers
- Negative numbers: [-10, 0, 10]
- Large numbers
- Zero values: [0, 0, 0]

Why focus on these?
- Measurements could come from sensors, user input, or external APIs with dirty data
- Type confusion (especially booleans) could silently corrupt calculations
- Applications require precise handling of edge cases
- Division by zero crashes need prevention
- None vs 0 distinction is important for downstream logic


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Original code does not safely handle mixed types
- Doesn't mention that booleans should be excluded
- The implementation will crash with type errors, not handle them safely
- No mention of empty list, all-None scenario, or return value choices

### Rewritten explanation
- This function calculates the average of valid numeric measurements from a list that may contain mixed types. It filters out None values, non-numeric types, and booleans. The boolean exclusion is necessary because in Python, bool is a subclass of int, meaning isinstance(True, int) returns True. Without explicit boolean checking, True would be treated as 1 and False as 0, corrupting the average. The function returns None if the input list is empty, and 0 if all values are invalid or None, and returns the calculated average otherwise. Only values that pass type validation contribute to both the sum and count, ensuring mathematical correctness.

## 4) Final Judgment
- Decision: Approve

- Justification: The function properly addresses all bugs from the original implementation. It includes explicit type checking with `isinstance(v, (int, float))` to prevent type errors, excludes booleans with `and not isinstance(v, bool)` to avoid treating True/False as 1/0, counts only valid measurements for the denominator ensuring mathematical correctness, handles empty input by returning None, and protects against division by zero when all values are invalid.

- Confidence & unknowns: High confidence. The code correctly handles all identified edge cases and follows best practices. Unknown: Preference for return values (None vs 0 vs exceptions for edge cases), whether exotic numeric types like Decimal or numpy arrays need support, and whether infinity/NaN values should be explicitly filtered.