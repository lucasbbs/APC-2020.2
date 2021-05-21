with open(input()) as f:
    lines = [line.strip() for line in f]
for i, line in enumerate(lines):
    hasPrincess = line.find("P")
    hasKnight = line.find("C")
    hasDragon = line.find("D")
    if hasPrincess != -1:
        positionPrincess = i
    if hasKnight != -1:
        positionKnight = i
    if hasDragon != -1:
        positionDragon = i
print(f"Princesa no andar {len([line for line in lines if line == '|-----------------|'])+1}")
print(f"Cavaleiro no andar {len([line for line in lines[positionKnight::] if line == '|-----------------|'])+1}")
print(f"Dragão no andar {len([line for line in lines[positionDragon::] if line == '|-----------------|'])+1}")

print('Quero ver descerem u.u' if(positionPrincess-positionDragon)/2 < (positionPrincess-positionKnight) else 'Mais um pro lanche!')
