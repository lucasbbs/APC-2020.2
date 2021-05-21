import json
def calcula_dic():
  tags = {}
  for each in dicionario["GraphImages"]:
      likes = each["edge_media_preview_like"]["count"]
      comments = each["edge_media_to_comment"]["count"]
      for tag in each['tags']:
          tags[tag] = tags.get(tag, {})
          tags[tag]['number'] = tags.get(tag, {}).get('number', 0) + 1
          tags[tag]["likes"] = tags.get(tag, {}).get('likes', 0) + likes
          tags[tag]["comments"] = tags.get(
              tag, {}).get('comments', 0) + comments
  return tags
def indice_de_engajamento(tagg,tags):
  return tags[tagg]['likes']+tags[tagg]['comments']*10

with open(input()) as f:
    dicionario = json.load(f)
tags = calcula_dic()
lista = []
print('Tags de',dicionario["GraphImages"][0]["username"])
for each in tags: lista.append((each, indice_de_engajamento(each, tags)))
[print(n[0], n[1]) for n in sorted(lista,key=lambda x: (-x[1], x[0]))]
