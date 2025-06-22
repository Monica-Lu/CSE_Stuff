def dec_to_bin(number):
    intpart = number.split(".")[0]
    decpart = number.split(".")[1]
    decpart = "0." + decpart

    intpart = int(intpart)
    decpart = float(decpart)

    intarray =[]
    decarray =[]

    while intpart > 1:
        if intpart % 2 == 0:
            intarray.insert(0, "0")
        else:
            intarray.insert(0, "1")
        intpart = intpart // 2

    intarray.insert(0, str(intpart))

    for i in range(21):
        decpart = decpart * 2
        if decpart < 1:
            decarray.append("0")
        else:
            decarray.append("1")
            decpart = decpart - 1

    return "".join(intarray) + "." + "".join(decarray)

if __name__ == "__main__":
    number = "10.023"
    print(dec_to_bin(number))
