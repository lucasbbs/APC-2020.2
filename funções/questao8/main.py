number1, number2, number3 = map(int, input().split())

def print_rectangle(number):
    print(number)
    print("+"*number)
    print(f"+{' '*(number-2)}+")
    print("+"*number)

print_rectangle(number1)
print_rectangle(number2)
print_rectangle(number3)
