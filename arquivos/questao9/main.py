# import json
# with open(input()) as f:
#     jsonData = json.load(f)
import apc
nome = input()
dicionario = apc.parser(nome)
tags = {}
print('Tags de',dicionario["GraphImages"][0]["username"])
for each in dicionario["GraphImages"]:
  for tag in each['tags']:
    tags[tag] = tags.get(tag, 0) + 1
for tag, number in tags.items():
    print(tag, number)

    
