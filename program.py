"""
tape = [
    14, 5, 0,  # set register to 5

    # index 3 for loop
    9, 0, 1,  # ram 0 += 1
    5, 0, 0,  # set display to ram 0
    200, 5, 0,  # show display
    19, -1, 0,  # subtract one from register
    100, 3, 1,  # jump to start of loop if 1 < register

    #index 18 for loop
    10, 0, 1,  # subtract 1 from ram 0
    5, 0, 0,  # set display 0 to 0
    200, 5, 0,  # show display (get rid of trailing 0's )
    19, 1, 0,  # add 1 to register
    103, 18, 1,  # jump index 18, if register != 1

    255, 0, 0  # end program
]
"""

tape = [

    # SET UP WORK
    # register to 0
    14, 0, 0,
    # ram0 to 5
    7, 0, 5,

    # LOOP START index: 6
    # set display to ram0
    5, 0, 0,
    # display
    200, 5, 0,
    # ram0 -= 1
    10, 0, 1,
    # register = ram0
    16, 0, 0,
    # jump to 6 if register != -1
    103, 6, -1,
    # LOOP END

    # end program
    255, 0, 0,



]
