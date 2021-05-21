number1, number2, number3 = map(int, input().split())

def print_rectangle(number):
    print(number)
    print("x"*number)
    print(f"x{' '*(number-2)}x")
    print(f"x{' '*(number-2)}x")
    print("x"*number)

print_rectangle(number1)
print_rectangle(number2)
print_rectangle(number3)
