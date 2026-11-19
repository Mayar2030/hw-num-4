amount_of_days = [5, 9, 4, 1, 6]


def checkabsence(x):
    for i in amount_of_days:
        if i > 5:
            return "woong woong you are blocked!"
        elif i <= 5:
            return "allowed!"
        elif i == str:
            return "we only accept numbers ya binti "


print(checkabsence(amount_of_days))
