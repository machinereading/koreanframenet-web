import json

indices = []

def make_key(string):
    return string.replace('-','').upper()

for i in range(1,5662) :
	f = open(str(i) + '.json')
	data = json.loads(f.read())

	f.close()
	indices.append({'lu':data['ko_lu'], 'pos':data['ko_pos'], 'id':i})

indices.sort(key=make_key)
print(indices[0]['lu'])
f = open('index.json', 'w')
f.write(json.dumps(indices))

f.close()
