base10_message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

inhex = hex(base10_message)[2:]

hexes_list = [f"0x{inhex[i : i + 2]}" for i in range(0, len(inhex), 2)]

print(hexes_list)

ascii_list = [int(value, 16) for value in hexes_list]

print(ascii_list)

word = "".join(chr(code) for code in ascii_list)

print(word)
