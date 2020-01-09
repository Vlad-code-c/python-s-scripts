import pandas as pd
data = []
i = 0

with open("m7-map-1.txt", 'r') as fp:
    data += fp.readlines()

id = []
coord = []
supr = []
spr = []

for d in data:
    if " :: " in d:
        spl = d.split(' :: ')
        id.append(spl[0])
        coord.append(spl[1].split(',', 1))
        supr.append(spl[2].split('x', 1))
all = {
    "id":id,
    "coord":coord,
    "supr":supr,
}
#print(f"id:{id[0]} coord:{coord[0]}  supr:{supr[0]}")
pdata = pd.DataFrame(all)


print(pdata)
#remove \n from supr (if it affect prog(str(supr)))
#resolve problem