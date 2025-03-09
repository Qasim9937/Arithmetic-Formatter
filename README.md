# Arithmetic Arranger

## Description
The `arithmetic_arranger` function formats simple arithmetic problems (addition and subtraction) in a visually structured manner. It supports up to five problems at a time and can optionally display the results.

## Features
- Accepts up to **five** arithmetic problems.
- Supports **addition (`+`) and subtraction (`-`)** operations.
- Ensures both operands contain **only digits** and have a maximum of **four digits**.
- Returns a formatted string displaying the problems in a vertically aligned layout.
- Allows the option to **show or hide answers**.

## Usage
```python
from arithmetic_arranger import arithmetic_arranger

# Example usage without answers
test_problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(test_problems))

# Example usage with answers
print(arithmetic_arranger(test_problems, show_answers=True))
```

## Example Output
Without answers:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

With answers:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```

## Error Handling
- If more than 5 problems are provided:
  ```
  "Error: Too many problems."
  ```
- If an operator other than `+` or `-` is used:
  ```
  "Error: Operator must be '+' or '-'."
  ```
- If any operand contains non-numeric characters:
  ```
  "Error: Numbers must only contain digits."
  ```
- If any operand is more than four digits long:
  ```
  "Error: Numbers cannot be more than four digits."
  ```

## License
This project is open-source and available for educational purposes.

