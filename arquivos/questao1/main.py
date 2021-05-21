import json
with open(input()) as f:
    jsonData = json.load(f)
for i,data in enumerate(jsonData["GraphImages"]):
    print("Publicacao numero", i+1)
    print(data["username"])
    print(data["edge_media_preview_like"]["count"]) 

