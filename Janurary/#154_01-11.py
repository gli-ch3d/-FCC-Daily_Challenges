## Par for the Hole
# 2026-01-11

def golf_score(par, strokes):
    lingo = {
        -2  :"Eagle",
        -1  :"Birdie",
        0   :"Par",
        1   :"Bogey",
        2   :"Double bogey"
    }
    if strokes == 1:
        val = "Hole in one!"
    else:
        val = lingo[strokes-par]
    return val