print(sum(map(ord, list(input()))))

def value(s):
    total = 0
    for ch in s:
        total += ord(ch)
    return total
s = input()
print(value(s))
