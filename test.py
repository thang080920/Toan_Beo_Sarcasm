import json
# with open("data.json") as file:
#     data = json.load(file)
# print(data)
keyword = []
file = open('./data.json', encoding="utf8")
data = json.load(file)

print(data['normal'][0]['text'])
list_data = []
for i in data['normal']:
    # print(i['text'])
    list_data.append(i['text'])
print(list_data)

for index in data['keys']:
    keyword.append(index['text'])
print(keyword)
file.close()