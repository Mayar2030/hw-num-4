scores = [50, 49, 55, 101, 20]


def checkgrades(x):
    for i in scores:
        if i > 100 or i == str:
            return "how is that possible"
        elif i < 50:
            return "ya salam you failed"
        elif i >= 50:
            return "ya salam you passed "


print(checkgrades(scores))
