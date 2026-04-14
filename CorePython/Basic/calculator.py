# Function to perform calculation
def calculate(n1, n2, op):
    if op == '+': return n1 + n2
    elif op == '-': return n1 - n2
    elif op == '*': return n1 * n2
    elif op == '/':
        return n1 / n2 if n2 != 0 else "Error: Division by zero"
    else: return "Invalid Operator"

# User Input
print("Simple Calculator")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Result
print("Result:", calculate(num1, num2, op))
