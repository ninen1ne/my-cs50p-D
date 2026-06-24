# while True:
#     n = int(input("what's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print('yoll')

def main():
    while True:
        print_menu()
        choice = get_int("what's choice? ")
        
        if choice not in [1, 2, 3, 4, -1]:
            print("Invalid User Input.")
            continue

        if choice == -1:
            break
        
        a = get_int("what's a? ")
        b = get_int("what's b? ")

        result = execute_calculation(choice, a, b)
        print(f"Result: {result}")
        
    print("-----EXIT PROGRAM-----")

def print_menu():
    print("""
    option: 1) plus
            2) minus
            3) multiply
            4) division
            -1) exit
    """)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error cannot divide by zero."
    return a / b

def execute_calculation(choice, a, b):
    match choice:
        case 1: return plus(a, b)
        case 2: return minus(a, b)
        case 3: return multiply(a, b)
        case 4: return division(a, b)

main()