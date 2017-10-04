checkerboard = "";
for i in range(0,8):
    checkerboard = ""
    for j in range(0,8):
        if (i%2 == 0):
            if (j%2 == 0):
                checkerboard += '*'
            else:
                checkerboard += ' '
        else:
            if (j%2 == 0):
                checkerboard += ' '
            else:
                checkerboard += '*'
    print(checkerboard)
