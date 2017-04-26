def dec_to_bit(dec):
    dec = int(dec)
    bit_list = []
    while dec > 0:
        bit = dec % 2
        dec //= 2
        bit_list.append(str(bit))
    bit_list.reverse()
    bit_number = ''.join(bit_list)
    return bit_number
#convers decimal to binnary

def bit_to_dec(bit):
    bit = [int(x) for x in str(bit)]
    power = len(bit) - 1
    dec_sum = 0
    for number in bit:
        dec_sum += number * (2 ** power)
        power -= 1
    dec_number = dec_sum
    return dec_sum
#converts binnary to decimal


def main():
    user_input = input("Input decimal or binnary numer, with operator 2 or 10 after space: ").split(" ")
    answer = None
    while len(user_input) != 2 or user_input[1] not in ["2", "10"] or not user_input[0].isdigit():
        user_input = input("invalid input. give another number ").split(" ")

    if user_input[1] == "10":
        user_input[0] = int(user_input[0])
        converted_number = dec_to_bit(user_input[0])

    elif user_input[1] == "2":
        while True:
            try:
                int(user_input[0], 2)
            except ValueError:
                user_input[0] = input("invalid number. give correct binnary number ")
            else:
                converted_number = bit_to_dec(user_input[0])
                break

    print(converted_number, user_input[1])

if __name__ == '__main__':
    main()
