import pandas

data = pandas.read_json("sample.json")
print(data["quiz"]["sport"]["q1"]["question"])
print(data["quiz"]["sport"]["q1"]["options"])
