for line in open("CW2014_02.in", "r"):
    gal = int(line)
    if gal == 0:
        break
    print("%d gallons per week will last %d weeks" % (gal, int(10000/gal)))
