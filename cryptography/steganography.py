# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes
class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None
    def encode(self, filein, fileout, message, codec):
        # return the pixel array of the image
        image = cv2.imread(filein)
        print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)
        # convert into binary
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == 'huffman':
            self.codec = HuffmanCodes(delimiter = self.delimiter)
        binary = self.codec.encode(message + self.delimiter) # encode the message to binary
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            
            # encode the message into the image file
            bin_count = 0
            for s in range(len(image)):
                for p in range(len(image[s])):
                    # check if the whole binary message has been encoded
                    if bin_count == len(self.binary):
                        break
                    
                    for c in range(len(image[s][p])):
                        # check if the whole binary message has been encoded
                        if bin_count == len(self.binary):
                            break
                        
                        # convert both to int data types to compare them
                        # when converted to binary an even number will always end in 0
                        # odd num will end in 1
                        # check if the number (odd or even) matchs the binary val
                        # if the number doesn't match add 1 to the number
                        if int(image[s][p][c] % 2) != int(self.binary[bin_count]):
                            # if the color band val is 255 then subtract 1 from the color band val
                            # otherwise add 1
                            if image[s][p][c] == 255:
                                image[s][p][c] -= 1
                            else:
                                image[s][p][c] += 1
                        
                        
                        bin_count += 1
            
            print(image)
            # return the new image file
            cv2.imwrite(fileout, image)
                       
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        print(image) # for debugging      
        
        flag = True
        # convert into text
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # pull the binary data from the image
            binary_data = ""
            
            found = False # flag for delimiter
            for s in range(len(image)):
                if found:
                    break
                for p in range(len(image[s])):
                    if found:
                        break
                    for c in range(len(image[s][p])):
                        # append a 0 if the color ban val is even
                        # 1 if it's odd
                        binary_data += str(image[s][p][c] % 2)
                            
            
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
            # get the encoded binary 
            binary = []        
            for i in range(0,len(binary_data),8):
                byte = binary_data[i: i+8]
                if byte == self.codec.encode(self.delimiter):
                    break
                binary.append(byte)
            
            # returing the right binary string
            if codec == 'caesar':
                binary = self.codec.bin_shift(binary)
            elif codec == 'huffman':
                if self.codec == None or self.codec.name != 'huffman':
                    print("A Huffman tree is not set!")
            self.binary = "".join(binary) 
            print()       
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          
    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()
        
