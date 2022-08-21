a = input(">>").split()
alternate = input("(a)>>")
spalternate = input("(b)>>")

'''
O O O O
O O O O
O O O O
O O O O
O O O O
'''

letter_locations = {}
letter_locations["a"] = ["OOO", "O O", "OOO", "O O", "O O"]
letter_locations["b"] = ["OO ", "O O", "OO ", "O O", "OO "]
letter_locations["c"] = ["OOO", "O  ", "O  ", "O  ", "OOO"]
letter_locations["d"] = ["OO ", "O O", "O O", "O O", "OO "]
letter_locations["e"] = ["OOO", "O  ", "OO ", "O  ", "OOO"]
letter_locations["f"] = ["OOO", "O  ", "OO ", "O  ", "O  "]
letter_locations["g"] = ["OOO", "O  ", "O O", "OOO", "  O"]
letter_locations["h"] = ["O O", "O O", "OOO", "O O", "O O"]
letter_locations["i"] = [" O ", " O ", " O ", " O ", " O "]
letter_locations["j"] = ["OOO", "  O", "  O", "O O", " O "]
letter_locations["k"] = ["O O", "O O", "OO ", "O O", "O O"]
letter_locations["l"] = ["O  ", "O  ", "O  ", "O  ", "OOO"]
letter_locations["m"] = ["O   O", "OO OO", "O O O", "O   O", "O   O"]
letter_locations["n"] = ["O  O", "OO O", "OOOO", "O OO", "O  O"]
letter_locations["o"] = [" OO ", "O  O", "O  O", "O  O", " OO "]
letter_locations["p"] = ["OOO ", "O  O", "OOO ", "O   ", "O   "]
letter_locations["s"] = [" OOO", "O   ", " OO ", "   O", "OOO "]
letter_locations["q"] = [" OO ", "O  O", "O  O", " OO ", "   O"]
letter_locations["r"] = ["OOO ", "O  O", "OOO ", "O O ", "O  O"]
letter_locations["t"] = ["OOO", " O ", " O ", " O ", " O "]
letter_locations["u"] = ["O  O", "O  O", "O  O", "O  O", " OO "]
letter_locations["v"] = ["O  O", "O  O", "O O ", "OO  ", "O   "]
letter_locations["x"] = ["O  O", "O  O", " OO ", "O  O", "O  O"]
letter_locations["w"] = ["O   O", "O   O", "O O O", "O O O", " O O "]
letter_locations["y"] = ["O  O", "O  O", " OO ", " O  ", "O   "]
letter_locations["!"] = [" O ", " O ", " O ", "   ", " O "]
letter_locations["?"] = ["OOOO", "   O", " OOO", "    ", " O  "]

letter_locations["."] = [" ", " ", " ", " ", ".", ]

buffer = ""
for word in a:
    word = word.lower()
    for i in range(5):
        buffer = ""
        for letter in word:
            letter_locations[letter][i] = letter_locations[letter][i].replace(
                " ", spalternate)
            buffer += letter_locations[letter][i].replace(
                "O", alternate) + spalternate
        print(buffer)
    print("")
