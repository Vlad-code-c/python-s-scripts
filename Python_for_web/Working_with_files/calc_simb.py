
symbol = '.'
sym_count = 0
word_count = 0
m = 0

fp = open("m5-line-by-line.txt", "r", encoding='utf-8')


line = fp.readline()
while len(line) != 0:
    for i in line:
        if i == symbol:
            sym_count += 1
        if i == ' ':
            word_count += 1
    line = fp.readline()


print("Words: " + str(word_count))
print("Words with symbol: " + str(sym_count))

procent = (word_count * sym_count) / 100
print("Procent of words with special symbol: " + str(int(procent)))