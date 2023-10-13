import os, random
def main():
    os.system('clear')
    line = "█"
    n = 196

    colors = [196, 197, 198, 199, 163, 164, 128, 129, 91, 92, 93, 56, 57, 21]

    colors_1 = [226, 227, 228, 229, 191, 192, 193, 194, 156, 157, 158, 159, 121, 122, 123, 86, 87, 51]

    colors_2 = [208, 209, 210, 211, 173, 174, 175, 176, 138, 139, 140, 141, 103, 104, 105, 68, 69, 33]

    colors_3 = [160, 196, 202, 208, 214, 220, 226]


    colors_A = [colors, colors_1, colors_2, colors_3]


    rannum = random.randint(2, 10)
    print("Progressbar: ", end='')
    for k in random.choice(colors_A):
        color = f"\u001b[38;5;{k}m"
        print(f"{color}{line * rannum}\x1b[0m", end='')
    input()
    main()

main()
