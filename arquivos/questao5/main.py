list_of_lists = []

with open(input()) as file:
  for line in file:
      stripped_line = line.strip()
      line_list = stripped_line.split()
      list_of_lists.append(line_list)
    
lines = [line[0].split(",") for line in list_of_lists]
[[print(line[1]) for i,word in enumerate(line) if i == len(line)-1] for line in lines]
