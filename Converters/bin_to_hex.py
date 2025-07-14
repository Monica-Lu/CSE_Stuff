def bin_to_hex(num):
    numarray = num.split(" ")
    bin_to_hex_map = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    hex_str = ""
    for items in numarray:
        hex_str += bin_to_hex_map.get(items, "?") #? for invalid
    return hex_str

if __name__ == "__main__":
    num = "1000 0101 0110 1010 0011"
    print(bin_to_hex(num))