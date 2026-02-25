from PIL import Image
from binary import *
from sys import argv
from os.path import exists

def usage() -> None:
    print('''
    Usage:
        python3 steg.py [options] <image_filename>

        Options:
            -e, --encode     Encode/Hide a message to the image_filename
            -d, --decode     Decode/Extract an image, by deafult, it prints to console ''')


def run():
    x = y = 100
    coordinates = (x,y)
    
    try:
        script, option, image_file, = argv
        if exists(image_file):
            image = Image.open(image_file)
            print('File okay')
        else:
            print('No such image file')
        if option == '-e' or option == '--encode':
            encode(image, input('Enter message:\n'), coordinates)
        elif option == '-d' or option == '--decode':
            print(readXterFromImage(image, coordinates))
        else:
            print('Option not found')
            usage()
            
    except ValueError as e:
        usage()
    
    
def getPixelBinary(image, coordinates):
    dec_values = image.getpixel(coordinates)
    bin_values = []
    for i in dec_values:
        bin_values.append(toBinary(i))
    #print(f'At pixel {coordinates}, RGB is {dec_values} or {bin_values}')
    return bin_values

def addXterToImage(image, xter, coordinates, continue_bit):
    ''' Takes a character, image and tuple of coodinates eg:
            last_pixel = addXterToImage('h', image, (10,10)) 
        Returns coordinate of last modified pixel'''
    new_x = new_y = 0     # set to  pixel 0,0 
    bin_xter = toBinary(xter) # bin_xter is '01101000' incase xter was 'h'
    bin_xter_toplace = []     # have a version with continue bit set e.g 'h' = ['011','010','001'] the last 1 is continue bit
    for i in range(0, 8, 3):  # To set i as index for 0,3,6 to be able to seperate 'h' and add continue bit
        sub  = '' 
        for z in range(0,3):
            reached_last_bit = i == 6 and z == 2
            if reached_last_bit and continue_bit:
                sub += '0'
            elif reached_last_bit and not continue_bit:
                sub += '1'
            else:
                sub += bin_xter[i+z]
        bin_xter_toplace.append(sub) # Now bin_xter_toplace = ['011', '010', '001'] incase continue_bit was False

    for pixel in range(0,3): # Get next three pixels from start coordinate
        new_x = coordinates[0]
        new_y = coordinates[1]+pixel
        bin_values = getPixelBinary(image, (new_x,new_y))  # Get the binary pixel values of 1st coordinate
        new_pix_values = []
        for color in range(0,3):  # Loop through RGB manipulating the least significant bit to 'h' value
            new_color = bin_values[color][:-1] + bin_xter_toplace[pixel][color]
            new_pix_values.append(fromBinaryToInt(new_color))
        
        image.putpixel((new_x,new_y), tuple(new_pix_values)) # Now change the values in the image
        #print(f'{new_x},{new_y} is \t\t{new_pix_values}')
        #print(f'{new_x},{new_y} was {}')
        
    return (new_x, new_y)

def encode(image, message, start_pixel):
    for i in range(0, len(message)):
        continue_bit = True if i != len(message) - 1 else False     # Check we haven't reached last message xter
        stop_pixel = addXterToImage(image, message[i], start_pixel, continue_bit)
        start_pixel = (stop_pixel[0], stop_pixel[1] + 1)
        #print(f'"{message[i]}" Stopped at {stop_pixel}')
        #print(f'{message[i+1]} will start at {start_pixel}') if i < len(message) -1 else print('Reached end of string')
#print(getPixelBinary(coordinates))

#encode('There is no end!!', (x,y))

def readXterFromImage(image, coordinates):
    # From the start coordinates, read the least significant bit from the colors exempting the alpha
    xter_bin = ''
    stopped_pixel = ()
    for pixel in range(0,3):  # Get three pixels that encode one character from coordinates
        new_x = coordinates[0]
        new_y = coordinates[1] + pixel
        color_values = image.getpixel((new_x, new_y))
        bin_values = []
        for color in color_values:   # change color decimal values to binary
            bin_values.append(toBinary(color))
        for color in range(0,3):     # Extract message excluding alpha channel
            xter_bin += bin_values[color][-1]    # Take last bit
        #print(f'At ({new_x},{new_y}) color is {bin_values}')
        stopped_pixel = (new_x,new_y)
    if xter_bin[-1] == '1':
        continue_bit = False
    else:
        continue_bit = True

    #print(f'Xter is {xter_bin[:-1]} and continue bit is {continue_bit}')
    return [fromBinaryToAscii(xter_bin[:-1]),continue_bit,stopped_pixel]
#output = readXterFromImage(image, (100,100))
#print(f'{output[0]} and can continue {output[1]} and stopped at {output[2]}')
#print(f'Next is {output[2][0]},{output[2][1]+1}')

if __name__ == '__main__':
    run()
