import pandas


def procent(num1, num2):
    return (num1 * num2) / 100



#timestamp,ip,user-agent
data = pandas.read_csv("m5-access-log-all.csv")
ip = data["ip"].value_counts().index[0]
count = data["ip"].value_counts()[0]
fraction = procent(count, int(data["ip"].count()))
last_time = data["timestamp"].value_counts().index[0]
last_agent = data["user-agent"].value_counts().index[0]


suspicious_agent = {
    "ip": ip,
    "fraction": fraction,
    "count":count,
    "last":{
        "agent":last_agent,
        "timestamp":last_time
    }
}

#print(suspicious_agent)