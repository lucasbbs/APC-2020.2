number = int(input())
with open('/etc/passwd') as f:
    lines = [line.strip().split(":") for line in f]
    
print(lines[number-1][0])
