import pandas

#Год,"Крупа манная, кг","Крупа гречневая-ядрица, кг"
data = pandas.read_csv("m5-buckwheat.csv")
print(data[0:5][["Крупа манная, кг", "Крупа гречневая-ядрица, кг"]].max())
