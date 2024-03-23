import math
import time
import compiledCode

# storage of 1000 bytes
global tape
global register
global jumpPoint
global display
global ram

tape = compiledCode.tape
register = 0

TAPE_LENGTH = 999
for i in range(TAPE_LENGTH - len(tape)):
    tape.append(0)
# ram (if -1, not in use)
ram = [0 for i in range(10)]

display = [0 for i in range(32)]



def operatingSystem():
    global register
    global tape
    global ram
    global display
    global jumpPoint
    print("start")
    debug = False
    i = 0
    output = open("output.txt", "w")
    while True:
        # add to index of next
        if tape[i] == 1:
            if debug:
                print("add to tape index: " + str(tape[i+1]))
            add(tape[i+1], tape[i+2])
        # sub from index of next
        if tape[i] == 2:
            if debug:
                print("subtract from tape index: " + str(tape[i + 1]))
            sub(tape[i+1], tape[i+2])
        # multiply to index of next
        if tape[i] == 3:
            if debug:
                print("multiply tape index: " + str(tape[i+1]))
            mult(tape[i+1], tape[i+2])
        # divide from index of next
        if tape[i] == 4:
            if debug:
                print("divide from tape index: " + str(tape[i + 1]))
            div(tape[i+1], tape[i+2])

        # set display index
        if tape[i] == 5:
            if debug:
                print("update display " + str(tape[i+1]) + " to " + str(ram[tape[i+2]]))
            updateDisplay(tape[i+1], ram[tape[i+2]])
        # set display index
        if tape[i] == 30:
            if debug:
                print("update display " + str(tape[i+1]) + " to " + str(tape[i+2]))
            updateDisplay(tape[i+1], tape[i+2])
        # clear display index
        if tape[i] == 6:
            if debug:
                print("clear display " + str(tape[i+1]))
            display[i+1] = 0

        # set ram index to next
        if tape[i] == 7:
            if debug:
                print("set ram index " + str(tape[i+1]) + " to " + str(ram[tape[i+2]]))
            ram[tape[i+1]] = tape[i+2]
        # clear ram index
        if tape[i] == 8:
            if debug:
                print("clear ram index " + str(tape[i+1]))
            ram[tape[i+1]] = 0
        # add to ram index
        if tape[i] == 9:
            if debug:
                print("add " + str(tape[i+2]) + " to ram index " + str(tape[i+1]))
            ram[tape[i+1]] += tape[i+2]
        # add to ram index
        if tape[i] == 10:
            if debug:
                print("sub " + str(tape[i + 2]) + " to ram index " + str(tape[i + 1]))
            ram[tape[i + 1]] -= tape[i + 2]
        # add to ram index
        if tape[i] == 11:
            if debug:
                print("mult " + str(tape[i + 2]) + " to ram index " + str(tape[i + 1]))
            ram[tape[i + 1]] *= tape[i + 2]
        # add to ram index
        if tape[i] == 12:
            if debug:
                print("div " + str(tape[i + 2]) + " to ram index " + str(tape[i + 1]))
            ram[tape[i + 1]] /= tape[i + 2]
        if tape[i] == 13:
            if debug:
                print("set ram index " + str(tape[i+1]) + " to register: " + str(register))
            ram[tape[i+1]] = register

        if tape[i] == 14:
            if debug:
                print("register set from tape index " + str(tape[i+1]) + ": " + str(tape[i+1]))
            register = tape[i+1]
        if tape[i] == 15:
            if debug:
                print("clear register")
            register = 0
        if tape[i] == 16:
            if debug:
                print("set register to " + str(ram[tape[i+1]]))
            register = ram[tape[i+1]]
        if tape[i] == 17:
            if debug:
                print("add " + str(tape[i+1]) + " to register")
            register -= ram[tape[i + 1]]
        if tape[i] == 18:
            if debug:
                print("sub " + str(ram[tape[i+1]]) + " from register")
            register -= ram[tape[i+1]]
        if tape[i] == 19:
            if debug:
                print("add " + str(tape[i+1]) + " to register")
            register += tape[i+1]

        # set index to next
        if tape[i] == 20:
            if debug:
                print("set index to " + str(tape[i+1]))
            i = tape[i+1]
        if tape[i] == 21:
            if debug:
                print(f'set index to ram[{tape[i+1]}]' + str(ram[tape[i+1]]))
            i = ram[tape[i+1]]
        if tape[i] == 22:
            if debug:
                print("set index to register: " + str(register))
            i = register

        # jump if > register
        if tape[i] == 100:
            if debug:
                print("jump to " + str(tape[i+1]) + " if " + str(tape[i+2]) + " > " + str(register))
            if tape[i+2] > register:
                i = tape[i+1]
                if debug:
                    print("jump completed")
                continue
        # jump if < register
        if tape[i] == 101:
            if debug:
                print("jump to " + str(tape[i+1]) + " if " + str(tape[i+2]) + " < " + str(register))
            if tape[i+2] < register:
                i = tape[i+1]
                if debug:
                    print("jump completed")
                continue
        # jump if == register
        if tape[i] == 102:
            if debug:
                print("jump to " + str(tape[i+1]) + " if " + str(tape[i+2]) + " == " + str(register))
            if tape[i+2] == register:
                i = tape[i+1]
                if debug:
                    print("jump completed")
                continue
        if tape[i] == 103:
            if debug:
                print("jump to " + str(tape[i+1]) + " if " + str(tape[i+2]) + " != " + str(register))
            if tape[i+2] != register:
                i = tape[i+1]
                if debug:
                    print("jump completed")
                continue
        if tape[i] == 106:
            if debug:
                print("set jump point to current position: " + str(i))
            jumpPoint = i+3
        if tape[i] == 107:
            if debug:
                print("set jump point to " + str(tape[i+1]))
            jumpPoint = tape[i+1]
        if tape[i] == 108:
            if register != tape[i+1]:
                if debug:
                    print("jump to last jump point")
                i = jumpPoint
                if debug:
                    print("jump completed")
                continue
            if debug:
                print("did not jump, reg != " + str(tape[i+1]))
        if tape[i] == 110:
            if debug:
                print("jump to " + str(tape[i+1]))
            i = tape[i+1]
            if debug:
                print("jump complete")
        if tape[i] == 200:
            if debug:
                print("show display")
            output.write(showDisplay(tape[i+1]) + "\n")
        if tape[i] == 201:
            if debug:
                print("show tape")
            showTape(tape)
        if tape[i] == 202:
            if debug:
                print("show ram")
            showRam(tape[i+1])
        if tape[i] == 203:
            if debug:
                print("show register")
            print(register)

        # print empty line
        if tape[i] == 205:
            print()

        if tape[i] == 210:
            debug = tape[i+1] == 0

        if tape[i] == 211:
            os.system('cls' if os.name == 'nt' else 'clear')

        if tape[i] == 255:
            print("exited")
            return  # exit out of loop
        i += 3
    output.close()


"""
    These are the functions that the tape will use to determine what to do
"""


def add(k, j):
    tape[k] += j
    tape[k] = tape[k] % 255


def sub(k, j):
    tape[k] -= j
    tape[k] = tape[k] % 255


def mult(k, j):
    tape[k] *= j
    tape[k] = tape[k] % 255


def div(k, j):
    tape[k] /= j
    tape[k] = tape[k] % 255


def toAlphanumeric(k):
    return chr(k)


def updateDisplay(k, j):
    display[k] = j


def showDisplay(x):
    # 1: get rid of trailing 0's
    # 2: change numerical to ascii characters
    # 4: combine into one string
    temp = display.copy()
    if x & 1 == 1:
        while len(temp) != 0 and temp[-1] == 0:
            temp.pop()
    if x & 2 == 2:
        for k in range(len(temp)):
            temp[k] = toAlphanumeric(temp[k])
    if x & 4 == 4:
        temp2 = ""
        for k in temp:
            temp2 = str(temp2) + str(k)
        temp = temp2
    # display requested frame
    print(temp)
    # return for output file
    return str(temp)


def wait(timeToWait):
    time.sleep(timeToWait/1000)


def showRam(x):
    temp = ram.copy()
    if x & 2 == 2:
        for k in range(len(temp)):
            temp[k] = toAlphanumeric(temp[k])
    if x & 4 == 4:
        temp2 = ""
        for k in temp:
            temp2 = str(temp2) + str(k)
        temp = temp2
    print(temp)


def showTape(tape):
    temp = tape.copy()
    while temp[-1] == 0:
        temp.pop()

    while len(temp) % 3 != 0:
        temp.append(0)

    for i in range(math.ceil(len(temp)/3)):
        print(temp[i*3], ": ", temp[i*3+1], ", ", temp[i*3+2])


operatingSystem()

