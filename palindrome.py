import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    print("User provided input:")
else:
    print("No command line input provided using manual input")
    text = "88"

# Check palindrome
if text == text[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
