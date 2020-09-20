CODE_TO_NAME = {"goldenrod": "#daa520", "GhostWhite": "#f8f8ff", "DarkViolet": "#9400d3", "DarkTurquoise": "#00ced1",
                "DarkSalmon": "#e9967a", "Orchid": "#9932cc", "chocolate": "#d2691e"}
print(CODE_TO_NAME)

colour_code = input("Enter colour name: ")
while colour_code != "":
    if colour_code in CODE_TO_NAME:
        print(colour_code, "-", CODE_TO_NAME[colour_code])
    else:
        print("Invalid colour name.")
    colour_code = input("Enter colour name: ")
