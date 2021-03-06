
string = """The merry old queen of Katoren has died
and there’s no heir to the throne. Six sour ministers rule the land
and claim that they’re looking for a new queen,
but nothing happens – for seventeen years. 
Then suddenly there’s a girl standing at the door of the royal
palace who was born on the night the queen died.

This girl, <name> , has firmly resolved to become the new queen of Katoren and
she asks the six ministers what she must do in order to be considered for 
the role. The ministers, afraid of losing their splendid position at court, give the
girl seven almost impossible tasks, which can be brought to a successful
conclusion only by one who possesses royal attributes such as wisdom,
courage and self-sacrifice. The six ministers are convinced that <name> will fall
at the first hurdle, but she turns out to have an amazing amount of
persistence and ingenuity.
"""

def change_name(line, name = "Mariana"):
    k = 0
    for t in line:
        if t == "<name>":
            l[k] = name
        k += 1
    return l

file = "queen_of_Katoren.txt"

with open(file, "w+") as f:
    for line in string.splitlines():
        if "<name>" in line:
            l = line.split()
            l = change_name(l)
            l = " ".join(l)
            line = l
        f.write(line + "\n")
