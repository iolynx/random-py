import random


def rn(lis): return range(len(lis))


def render(canvas):
    for i in rn(canvas):
        for k in range(len(canvas[i])):
            print(canvas[i][k], end=' ')
        print()


def paint_onto_canvas(canvas, painting, paint):
    for i in painting:
        canvas[i[0]][i[1]] = paint[random.randint(0, len(paint) - 1)]


canvas = []
for i in range(50):
    canvas.append(['.']*80)

#canvas[2][5] = "O"
#canvas[y][x] = "O"


def createTree(canvas):
    #trunk = #
    # leaf = ;
    init_length = 12
    trunk_width = 3
    leaf_width = 14
    WIDTH = len(canvas[0])
    HEIGHT = len(canvas)
    trunk_coords = []
    prevoffset, offset = 0, 0

    for i in range(27):
        if random.randint(0, 5) == 1:
            offset = prevoffset + random.randint(-1, 1)
        for k in range(trunk_width - i//9):
            trunk_coords.append(
                [HEIGHT - i - 1, WIDTH//2 - trunk_width + k + offset])

            if random.randint(0, 1) == 1 and i > 16 and i != 28:
                starting_point1 = random.randint(0, 28 - i)
                starting_point2 = random.randint(0, 28 - i)

                for l in range(random.randint(1, 4)):
                    trunk_coords.append(
                        [HEIGHT - i - 1 - l, WIDTH//2 - trunk_width + k + l + offset + starting_point1])

                    trunk_coords.append(
                        [HEIGHT - i - 1 - l, WIDTH//2 - trunk_width + k - l + offset - starting_point2])

        prevoffset = offset

    # NOW TO MAKE THE FUCKING LEAVES
    leaf_coords = []
    prev_width_offset, width_offset = 0, 0
    d_width_offset = 0
    dd_width_offset = 0
    for i in range(38):

        d_width_offset += dd_width_offset
        width_offset += d_width_offset
        width_offset = int(width_offset)

        # hmm s, this is kinematix
        if random.randint(0, 4) == 1:
            offset = prevoffset + random.randint(-3, 3)
        if i == 0:
            d_width_offset = 7
            dd_width_offset = -0.6
        elif i == 9:
            d_width_offset = 3
            dd_width_offset = -0.2
        elif i == 18:
            d_width_offset = 1
            dd_width_offset = -0.5
        elif i == 35:
            d_width_offset = -5
            dd_width_offset = -8.8

        for k in range(width_offset + 4 + random.randint(-3, 3)):
            leaf_coords.append(
                [i + 8, WIDTH//2 - width_offset // 2 + k + offset - random.randint(-2, 2)])
        prevoffset = offset

    paint_onto_canvas(canvas, leaf_coords, [";", "+", "/"])
    paint_onto_canvas(canvas, trunk_coords, ["#", "W", "M"])


createTree(canvas)

render(canvas)
