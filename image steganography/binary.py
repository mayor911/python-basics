''' This file converts to and from binary '''
def toBinary(xter) -> str:
    ''' Takes a string xter and returns its binary string value '''
    try:
        no = ord(xter)
    except TypeError as e:
        no = xter
    binary = ''
    dividers = {'bit8': 128, 'bit7': 64, 'bit6': 32, 'bit5': 16,
                'bit4': 8, 'bit3': 4, 'bit2': 2, 'bit1': 1}
    # create th byte hence range has to be 8
    bit = 8
    for i in range(8):
        divider = dividers[f'bit{bit}']
        if no >= divider:
            binary += '1'
            no %= dividers[f'bit{bit}']
        else:
            binary += '0'
        bit -= 1

    return binary

def fromBinaryToAscii(binary_string) -> str:
    ''' Takes binary string and returns ascii string value '''
    dividers = {'bit8': 128, 'bit7': 64, 'bit6': 32, 'bit5': 16,
                'bit4': 8, 'bit3': 4, 'bit2': 2, 'bit1': 1}
    bit_index = 8
    no = 0

    for bit in binary_string:
        if bit == '1':
            no += dividers[f'bit{bit_index}']
        bit_index -= 1
    return chr(no)

def fromBinaryToInt(binary_string) -> str:
    ''' Takes binary string and returns ascii string value '''
    dividers = {'bit8': 128, 'bit7': 64, 'bit6': 32, 'bit5': 16,
                'bit4': 8, 'bit3': 4, 'bit2': 2, 'bit1': 1}
    bit_index = 8
    no = 0

    for bit in binary_string:
        if bit == '1':
            no += dividers[f'bit{bit_index}']
        bit_index -= 1
    return no


def fromBinary(binary_string) -> str:
    ''' Takes binary string and returns ascii string value '''
    dividers = {'bit8': 128, 'bit7': 64, 'bit6': 32, 'bit5': 16,
                'bit4': 8, 'bit3': 4, 'bit2': 2, 'bit1': 1}
    bit_index = 8
    no = 0

    for bit in binary_string:
        if bit == '1':
            no += dividers[f'bit{bit_index}']
        bit_index -= 1
    return chr(no)

if __name__ == '__main__':
    xter = 's'
    byte = toBinary(xter)
    print(f'{xter} == {byte} ')
    print(f'And {byte} to ascii is {fromBinary(byte)}')
			
			
