import cv2
import numpy as np
import os

"""
Least Significant Bit (LSB) is a technique in which last bit of each pixel is modified and replaced with the data bit. 
This method only works on Lossless-compression images, which means that the files are stored in a compressed format, but that this compression does not result in the data being lost or modified, PNG, TIFF, and BMP as an example, are lossless-compression image file formats.
As you may already know, an image consists of several pixels, each pixel contains three values (which are Red, Green, Blue), these values range from 0 to 255, in other words, they are 8-bit values. For example, a value of 225 is 11100001 in binary and so on.
"""



def to_bin(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")


def encode(image_name, secret_data):
    # read the image
    image = cv2.imread(image_name)
    # maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("[*] Maximum bytes to encode:", n_bytes)
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    print("[*] Encoding data...")
    # add stopping criteria
    secret_data += "====="
    data_index = 0
    # convert data to binary
    binary_secret_data = to_bin(secret_data)
    # size of data to hide
    data_len = len(binary_secret_data)
    
    for row in image:
        for pixel in row:
            # convert RGB values to binary format
            r, g, b = to_bin(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # least significant red pixel bit
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant green pixel bit
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant blue pixel bit
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break
    return image


def decode(image_name):
    print("[+] Decoding...")
    # read the image
    image = cv2.imread(image_name)
    binary_data = ""
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    # split by 8-bits
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break
    return decoded_data[:-5]

"""
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Steganography encoder/decoder, this Python scripts encode data within images.')
    parser.add_argument('-t', '--text', help='The text data to encode into the image, this only should be specified for encoding')
    parser.add_argument('-e', '--encode', help='Encode the following image')
    parser.add_argument('-d', '--decode', help='Decode the following image')
    args = parser.parse_args()
   secret_data = args.text
    if args.encode:
        # if the encode argument is specified
        input_image = args.encode
        print('input_image:', input_image)
        # split the absolute path and the file
        path, file = os.path.split(input_image)
        # split the filename and the image extension
        filename, ext = file.split(".")
        output_image = os.path.join(path, f"{filename}_encoded.{ext}")
        # encode the data into the image
        encoded_image = encode(image_name=input_image, secret_data=secret_data)
        # save the output image (encoded image)
        cv2.imwrite(output_image, encoded_image)
        print("[+] Saved encoded image.")

    if args.decode:
        input_image = args.decode
        # decode the secret data from the image
        decoded_data = decode(input_image)
        print("[+] Decoded data:", decoded_data)
"""

def encode_main(file,path=""):
    #file = "download.png"
    filename, ext = file.split(".")
    encoded_image = encode(image_name=file, secret_data="Welcome")
    output_image = os.path.join(path, f"{filename}_encoded.{ext}")
    cv2.imwrite(output_image, encoded_image)
    print("[+] Saved encoded image.")

def decode_main(file):
    decoded_data = decode(file) #'download_encoded.png'
    print("[+] Decoded data:", decoded_data)

#encode_main()
#decode_main()