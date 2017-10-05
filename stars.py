
def draw_stars(arr):
    for i in arr:
        row = ""
        char = "*"
        if type(i) == str:
            char = i[0].lower()
            i = len(i)
        for j in range(i):
            row = row + char
        print(row)

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
