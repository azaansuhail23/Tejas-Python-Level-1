for row in range(5):
    letter = "A"

    for col in range(row):
        print(letter, end="")

        letter = chr(ord(letter) + 1)

    print()
