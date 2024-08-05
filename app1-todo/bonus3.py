def parse(feet_inches):
    parts=feet_inches.split(" ") #split() method stores feet and inches in a list format
    feet=float(parts[0])
    inches=float(parts[1])
    return {"feet": feet, "inches": inches} #returns feet and inches


def convert(feet, inches):
    meters = feet * 0.3048+ inches * 0.0254
    return meters