with open("CW2016_03.in", "r") as f:
    line = f.readline()
    count = int(line)
    for i in range(count):
        word = f.readline().strip()
        prev = word[0]
        likes = False
        for char in word[1:]:
            if prev == char:
                likes = True
            prev = char
        if likes:
            print("likes ", word)
        else:
            print("hates ", word)
