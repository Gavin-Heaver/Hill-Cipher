'''============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Gavin Heaver
| Language: python
| To Compile: javac pa01.java
| gcc -o pa01 pa01.c
| g++ -o pa01 pa01.cpp
| go build pa01.go
| rustc pa01.rs
| To Execute: python -> python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: CIS3360 - Security in Computing - Spring 2025
| Instructor: McAlpin
| Due Date: 02/25/2025
+==========================================================================='''
#Place all imports here
import sys

def main():
    
    #Initialize variables
    plaintext = ""
    cipherText = ""
    maxCharacters = 80
    
    #Get the file names from the command line
    keyFile = sys.argv[1]
    plaintextFile = sys.argv[2]
    
    #Open the files from the command line
    key = open(keyFile, "r")
    plain = open(plaintextFile, "r")
    
    #Initialize the key matrix
    keyMatrix = []
    
    #Get the size of the matrix
    matrixSize = int(key.readline())
    
    #Loop for row size
    for row in range(matrixSize):
        #Create a temporary array
        temp = []
        
        #Loop for column size, same as row size
        for column in range(matrixSize):
            #See if the number is 3 digits long
            try:
                temp.append(int(key.read(3)))
                
            #If it failed, go back 3 characters in the file to reset position    
            except ValueError:
                key.seek(key.tell()-3)
                
                #See if the number is 2 digits long
                try:
                    temp.append(int(key.read(2)))
                    
                #If it failed, go back 2 characters in the file to reset position    
                except ValueError:
                    key.seek(key.tell()-2)
                    
                    #Read the next value at 1 character length
                    temp.append(int(key.read(1)))
    
        
        #append the temp array values to the key matrix
        keyMatrix.append(temp)          
    
    #Print out the fact that the matrix will be output, along with its size
    print("\nKey matrix:")
    
    #Print out the matrix
    for row in range(matrixSize):
        for column in range(matrixSize):
        #print the value with some spacing for each column
            print("%4d" % keyMatrix[row][column], end = "")
        #make a space between each row
        print()
    
    #Create a spacer between the matrix and plaintext
    print() 
    
    #Read the plaintext in straight from the file
    plaintext = str(plain.read().replace('\n',''))
    
    #list valid letters for the plaintext
    valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #Remove all parts of plaintext except for the letters
    plaintextLower = ''.join(char for char in plaintext if char in valid_characters)
    
    #set the plaintext to lower
    plaintextLower = plaintextLower.lower()
    
    #Check to see if you have to add any x's
    while (len(plaintextLower) % matrixSize != 0):
        #add an x to the end of the 
        plaintextLower += 'x'
        
    #print out the fixed plaintext
    print("Plaintext:")  
    
    #Only print 80 characters at a time  
    for i in range(0, len(plaintextLower), maxCharacters):
        print(plaintextLower[i:i + maxCharacters])
      
    #Create a spacer between the plaintext and ciphertext
    print()
    
    #Create a matrix that will store the values each character has in the text
    cipherMatrix1 = []
    
    #Loop for the column size
    for i in range(int(len(plaintextLower)/matrixSize)):
        
        #Loop to increase i each turn by 1 less than matrixsize, allowing to go through entire matrix correctly
        for j in range(i):
            
            #Increase matrix size
            i += int(matrixSize-1)
            
        #Create a temp array    
        temp = []
        
        #Loop for the row size
        for j in range(matrixSize):
            
            #Get the Unicode for each character, and subtract by 97 to make it match the correct corresponding value, adding it to temp
            temp.append((ord(plaintextLower[i]) - 97))
            
            #Increase i by 1 to go to next index 
            i += 1
            
        #Add the temps to the first cipherMatrix    
        cipherMatrix1.append(temp)
    
    #Create a second matrix that will store the matrix multiplication result
    cipherMatrix2 = [[0 for rows in range(matrixSize)]for rows in range(int(len(plaintextLower)/matrixSize))]
    
    #Loop the amount of rows there are in the first cipherMatrix
    for i in range(int(len(plaintextLower)/matrixSize)):
    
        #Loop for the amount of characters in each array of the cipher Matrix
        for j in range(len(cipherMatrix1[0])):
        
            #Loop for the size of the key matrix
            for k in range(len(keyMatrix)):
                
                #Do the matrix multiplication
                cipherMatrix2[i][j] += cipherMatrix1[i][k] * keyMatrix[j][k]
    
    #Loop the amount of rows there are in cipher matrix
    for i in range(int(len(plaintextLower)/matrixSize)):
    
        #Loop for the size of each array in the cipher matrix
        for j in range(matrixSize):
            
            #Make conditional while the value stored at that spot in the matrix is greater than 25
            while cipherMatrix2[i][j] > 25:
            
                #Subtract 26 from it
                cipherMatrix2[i][j] -= 26
                
            #Now that it is greater than 25    
            if cipherMatrix2[i][j] <= 25:
                #Add the 97 back to it, and get the corresponding letter through the respective Unicode
                cipherText += (chr(cipherMatrix2[i][j] + 97))
    
    
    #print out the cipherText, with each line being 80 characters long
    print("Ciphertext:")
    for i in range(0, len(plaintextLower), maxCharacters):
        print(cipherText[i:i + maxCharacters])
    
    #Close the files
    key.close()
    plain.close()
    

main()


'''=============================================================================
| I Gavin Heaver (ga518853) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================='''

