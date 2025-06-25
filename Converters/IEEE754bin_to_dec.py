from bin_to_dec import int_bin_to_dec, dec_bin_to_dec

def half_prec(sign, exp, mantissa):
    result = 0.0
    #Process exp, zero offset = 15, exp = 5 bits
    bitshift = int(int_bin_to_dec(exp)) - 15

    #Process mantissa, mantissa = 10 bits
    mantissadec = 1 + dec_bin_to_dec(mantissa)

    #Process sign, sign = 1 bit
    if int(sign) == 1:
        sign = -1
    elif int(sign) == 0:
        sign = 1

    result = sign * (2**bitshift) * mantissadec

    return result

def single_prec(sign, exp, mantissa):
    result = 0.0
    #Process exp, zero offset = 127, exp = 8 bits
    bitshift = int(int_bin_to_dec(exp)) - 127

    #Process mantissa, mantissa = 23 bits
    mantissadec = 1 + dec_bin_to_dec(mantissa)

    #Process sign, sign = 1 bit
    if int(sign) == 1:
        sign = -1
    elif int(sign) == 0:
        sign = 1

    result = sign * (2**bitshift) * mantissadec

    return result

def double_prec(sign, exp, mantissa):
    result = 0.0
    #Process exp, zero offset = 1023, exp = 11 bits
    bitshift = int(int_bin_to_dec(exp)) - 1023

    #Process mantissa, mantissa = 52 bits
    mantissadec = 1 + dec_bin_to_dec(mantissa)

    #Process sign, sign = 1 bit
    if int(sign) == 1:
        sign = -1
    elif int(sign) == 0:
        sign = 1

    result = sign * (2**bitshift) * mantissadec

    return result

if __name__ == "__main__":
    num = "0 10000 1000000010" # example num in half_prec
    num = "0 10000000 10000000000000000010010" # example num in single_prec
    num = "1 10000000000 1100000001011000000010110000000101100000001010000000" # example num in double_prec

    sign = num.split(" ")[0]
    exp = num.split(" ")[1]
    mantissa = num.split(" ")[2]

    if len(num) == 18: #16bits + 2*" "
        if len(sign) != 1:
            print("error in sign bits in IEEE-754 Half Precision(16-bits)")
        elif len(exp) != 5:
            print("error in exp bits in IEEE-754 Half Precision(16-bits)")
        elif len(mantissa) != 10:
            print("error in mantissa bits in IEEE-754 Half Precision(16-bits)")
        else:
            print(half_prec(sign, exp, mantissa))
    elif len(num) == 34: #32bits + 2*" "
        if len(sign) != 1:
            print("error in sign bits in IEEE-754 Single Precision(32-bits)")
        elif len(exp) != 8:
            print("error in exp bits in IEEE-754 Single Precision(32-bits)")
        elif len(mantissa) != 23:
            print("error in mantissa bits in IEEE-754 Single Precision(32-bits)")
        else:
            print(single_prec(sign, exp, mantissa))
    elif len(num) == 66: #64bits + 2*" "
        if len(sign) != 1:
            print("error in sign bits in IEEE-754 Double Precision(64-bits)")
        elif len(exp) != 11:
            print("error in exp bits in IEEE-754 Double Precision(64-bits)")
        elif len(mantissa) != 52:
            print("error in mantissa bits in IEEE-754 Double Precision(64-bits)")
        else:
            print(double_prec(sign, exp, mantissa))
    else:
        print("error in the entire number length")