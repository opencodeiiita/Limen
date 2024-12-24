from PIL import Image
import sys
import numpy as np
import base64, cv2

def binary_to_int(binary):
    #converting binary to integer
    integer, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        integer = integer + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (integer)

def decimal_to_base64(integer):
    # Convert the integer value to bytes 
    byte_representation = integer.to_bytes((integer.bit_length() + 7) // 8, byteorder='big')
    # Encode the bytes to Base64
    base64_encoded = base64.b64encode(byte_representation).decode('utf-8')
    return base64_encoded

def NumMyImg():
    
    #Takes the input image path and the outfile file
    args = sys.argv
    i_file = args[1] #input image path
    o_file = args[2] #output file path


    #checks if the provided input file is some kind of image or not
    if (i_file[-3:] not in ["jpg","png","bmp"]):
        print("Correct Image File is not provided...")
        return
    
    if o_file[-4:] != ".txt":
         print("Output file is not valid, Give a .txt file")
         return
    
    #tries to open the given image file if provided correctly, checks if it is present or not
    try:
        with Image.open(i_file) as img:
            if ".bmp" not in i_file:
                    #first converting to bmp file then grascaling
                    img = img.convert("1")
                    img = img.convert("L")
                    data = np.array(img)

            else:
                    img = img.convert("L")
                    data = np.array(img)

    except FileNotFoundError:
        print("File is not Found, please enter correct image_path")
        return


    #Checks edge cases of black and white images
    flat_data = data.flatten()

    if np.all(flat_data == 255):
         print("Full White Image is Provided...")
         return
    elif np.all(flat_data == 0):
         print("Full Black Image is Provided...")
         return
    
    #for binarisation of image 128 is set as the threshold value
    newdata = np.floor(data/ 128)
    
    #If want to save the bmp image, code is written below
    #cv2.imwrite("out.png",( newdata)*255 )
    
    
    newdata = newdata.astype(int)
    bi_str = ''.join(newdata.astype(str).flatten())

    #An error was occuring regarding max length of digits...
    sys.set_int_max_str_digits(0)


    bi = int(bi_str)
    deci_eq = binary_to_int(bi)
    encoded = decimal_to_base64(deci_eq)


    #ecoded data is written in a txt type file given by the user
    with open(o_file, "w") as file:
        file.write(encoded)

    print(f"Encoded data written in {o_file} file...Successfully")


NumMyImg()
