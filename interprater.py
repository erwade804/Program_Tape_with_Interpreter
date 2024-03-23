

def interpret():
    f = open("toInterpret.txt", "r")
    allLines = f.read().split("\n")
    lines = []
    for i in allLines:
        if i != "":
            lines.append(i)
    cop = lines
    lines = []
    for i in cop:
        if " //" in i:
            i = i.split(" //")[0]
        if "//" in i:
            i = i.split("//")[0]
        i = removeWhiteSpace(i)
        lines.append(i)

    # get rid of anything after the // symbol
    # that will be the comment for the language

    linesString = "tape = ["
    for i in lines:
        linesString += "\n    "
        if "set reg to ram " in i:  # 16
            linesString += f'16, {i.split(" ")[-1]}, 0'
        elif "set ram " in i and " to reg" in i:
            linesString += f'13, {i.split("ram ")[-1].split(" ")[0]}, 0'
        elif "add " in i and " to tape " in i:
            linesString += f'1, {i.split(" ")[-1]}, {i.split("add ")[-1].split(" to tape ")[0]}'
        elif "subtract " in i and " from tape " in i:
            linesString += f'2, {i.split(" ")[-1]}, {i.split("subtract ")[-1].split(" from tape ")[0]}'
        elif "multiply " in i and " to tape " in i:
            linesString += f'3, {i.split(" ")[-1]}, {i.split("multiply ")[-1].split(" to tape ")[0]}'
        elif "divide " in i and " from tape " in i:
            linesString += f'4, {i.split(" ")[-1]}, {i.split("divide ")[-1].split(" from tape ")[0]}'
        elif "clear display " in i:
            linesString += f'6, {i.split(" ")[-1]}, 0'
        elif "set display " in i and " to ram " in i:
            linesString += f'5, {i.split("set display ")[-1].split(" to")[0]}, {i.split(" ")[-1]}'
        elif "set display " in i:
            linesString += f'30, {i.split(" to ")[0].split(" ")[-1]}, {i.split(" to ")[-1]}'
        elif "set reg to " in i:
            linesString += f'14, {i.split(" ")[-1]}, 0'
        elif "clear reg" in i:
            linesString += "15, 0, 0"
        elif "clear ram " in i:
            linesString += f'8, {i.split(" ")[-1]}, 0'
        elif "add ram " in i and " to reg" in i:
            linesString += f'17, {i.split("add ram ")[-1].split(" ")[0]}, 0'
        elif "add " in i and " to ram " in i:
            linesString += f'9, {i.split(" ")[-1]}, {i.split(" to ram ")[0].split(" ")[-1]}'
        elif "multiply " in i and " to ram " in i:
            linesString += f'11, {i.split(" ")[-1]}, {i.split(" to ram ")[0].split(" ")[-1]}'
        elif "divide " in i and " from ram " in i:
            linesString += f'12, {i.split(" ")[-1]}, {i.split(" from ram ")[0].split(" ")[-1]}'
        elif "subtract " in i and " from ram " in i:
            linesString += f'10, {i.split(" ")[-1]}, {i.split(" from ram ")[0].split(" ")[-1]}'
        elif "set ram " in i:
            linesString += f'7, {i.split(" to ")[-2].split(" ")[-1]}, {i.split(" to ")[-1]}'
        elif "add " in i and " to reg" in i:
            linesString += f'19, {i.split("add ")[-1].split(" ")[0]}, 0'
        elif i == "set jump point":
            linesString += "106, 0, 0"
        elif "set jump point" in i:
            linesString += '106, 0, 0'
        elif "jump if != " in i:
            linesString += f'108, {i.split(" ")[-1]}, 0'
        elif "show display" in i:
            sumOfOptions = 0
            if "options" in i:
                options = [int(j) for j in i.split("options ")[1].split(",")]
                for j in options:
                    sumOfOptions += j
            linesString += f'200, {sumOfOptions}, 0'
        elif "clear terminal" in i:
            linesString += "211, 0, 0"
        elif "end" in i:
            linesString += "255, 0, 0"
        else:
            linesString += i
        linesString += ","
    linesString += "\n]\n"
    f = open("compiledCode.py", "w")
    f.write(linesString)
    f.close()


def removeWhiteSpace(string):
    while string[-1] == " ":
        string = string[0:-1]
    return string


interpret()
