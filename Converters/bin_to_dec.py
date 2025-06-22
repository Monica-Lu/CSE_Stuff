def float_bin_to_dec(num):
    intpart = num.split(".")[0]
    decpart = num.split(".")[1]

    intdec = int_bin_to_dec(intpart)
    decdec = dec_bin_to_dec(decpart)

    return (intdec + decdec)

def int_bin_to_dec(intnum):
    intdec = 0
    for i in range(len(intnum)):
        intdec = intdec + int(intnum[i]) * 2 ** (int(len(intnum)) - 1 - i)

    return intdec

def dec_bin_to_dec(floatnum):
    decdec = 0.0

    for i in range(len(floatnum)):
        decdec = decdec + float(floatnum[i]) * 2 ** ((i + 1)* -1)

    return decdec

if __name__ == "__main__":
    num = "100010.0101010001"
    print(float_bin_to_dec(num))
    num = "11000" 
    print(int_bin_to_dec(num))
    num = "10100101" # stands for "0." + num
    print(dec_bin_to_dec(num))
