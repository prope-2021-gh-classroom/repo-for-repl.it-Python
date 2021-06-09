
#En este código se resulve el inciso b)
import re

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

file = "intento_1b.txt"

newname="Mariana"

with open(file, "w+") as f:
    for line in string.splitlines():
        if "<name>" in line:
            
            line = re.sub("<name>", newname, line) # Tercer argumento? creo así pedimos que se haga la subt de name por newname en "l"
            #l = change_name(l)  #segun yo aquí hay que cambiar 
            #l = " ".join(l)
            #line = l
        f.write(line + "\n")

#####################
# Creo que ya quedó #
#####################
# El problema era que en la función del inciso a) se estaba partiendo 
# cada línea en una lista. El método re.sub() funciona con cadenas de caracteres