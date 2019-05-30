import re

# 42536258796157867       #17 digits in card number → Invalid 
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

validator = re.compile(r"^"
                       r"(?!.*(\d)(-?\1){3})"
                       r"[456]"  # Doesn't start with 4, 5 or 6 → Invalid
                       r"\d{3}"  # Contains non digit characters → Invalid
                       r"(?:-?\d{4}){3}"
                       r"$")

for _ in range(int(input().strip())):
    print("Valid" if validator.search(input().strip()) else "Invalid")