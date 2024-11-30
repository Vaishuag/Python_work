def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Example usage:
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))
print("The Simple Interest is:", calculate_simple_interest(principal, rate, time))
