import random

Disney = ["Mickey","Minnie","Donald","Daisy","Goofy","Pluto"]
random.shuffle(Disney)
print(Disney)

Output = ""
for x in range(len(Disney)):
    if x == 0:
        Output += f"{Disney[x]}"
    elif x == len(Disney) - 1:
        Output += f" and {Disney[x]}."
    else:
        Output += f", {Disney[x]}"
print(Output)
