sum = 0

with open("m5-calibration.dat") as fp:
    for i in fp:
        sum += int(i)

print(sum)