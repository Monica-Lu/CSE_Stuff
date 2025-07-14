def hex_to_bin(num):
    hex_to_bin_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
    bin_str = ""
    for bitnum in num:
        bin_str += hex_to_bin_map.get(bitnum, "?") + " " #? for invalid
    return bin_str

if __name__ == "__main__":
    num = "0100ABE5"
    print(hex_to_bin(num))