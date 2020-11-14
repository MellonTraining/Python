def PrintRed():
    print("You chose red!\r\n")
def PrintGreen():
    print("You chose green!\r\n")
def PrintBlue():
    print("You chose blue!\r\n")
ColorSelect = {
    0: PrintRed,
    1: PrintGreen,
    2: PrintBlue,  
}
Selection = 0
while (Selection != 3):
    print("0. red")
    print("1. green")
    print("2. blue")
    print("3. Quit")
    Selection = int(input("Select a color option: "))
    if (Selection >= 0) and (Selection < 3):
        ColorSelect[Selection]()
