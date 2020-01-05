import pandas
import sqlite3

def procent(num1, num2):
    return (num1 / num2) * 100


cnx = sqlite3.connect('access_log.db')

df = pandas.read_sql_query("SELECT * FROM logs", cnx)
bd_uid = df["uid"]
bd_ip_addr = df["ip_addr"]
bd_timestamp = df["timestamp"]



bd_dates = {'uid':bd_uid, 'ip_addr':bd_ip_addr, 'timestamp':bd_timestamp}
data_tuples = list(zip(bd_uid, bd_ip_addr, bd_timestamp))

data = pandas.DataFrame(data=data_tuples, columns=['uid', 'ip_addr', 'timestamp']) 

i = 5
while i > 0:
    ip = data["ip_addr"].value_counts().index[i]
    count = data["ip_addr"].value_counts()[i]
    fraction = procent(count, data["ip_addr"].count())
    fraction = float("{:10.2f}".format(fraction))
    last_time = data["timestamp"].value_counts().index[i]

    suspicious_agent = {
        "ip": ip,
        "fraction": fraction,
        "count":count,
        "last":last_time
    }
    print(suspicious_agent)
    i -= 1



