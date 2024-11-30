def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage:
num = int(input("Enter a number: "))
print("The number is:", check_number(num))
