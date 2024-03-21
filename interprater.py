
f = open("toInterprate.txt", "r")
allLines = f.read().split("\n")
lines = []
for i in allLines:
    if i != "":
        lines.append(i)
print(lines)

linesString = ""
for i in lines:
    linesString += i+"\n"

f = open("compiledCode.py", "w")
f.write(linesString)
f.close()
