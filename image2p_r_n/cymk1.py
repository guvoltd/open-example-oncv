import cv2
import numpy as np
import csv


# Load image
bgr = cv2.imread('./testimg/bird1.jpg')

height = bgr.shape[0]
width = bgr.shape[1]
channels = bgr.shape[2]

# Make float and divide by 255 to give BGRdash
bgrdash = bgr.astype(np.float64)/255.

# Calculate K as (1 - whatever is biggest out of Rdash, Gdash, Bdash)
K = 1 - np.max(bgrdash, axis=2)

# Calculate C
C = (1-bgrdash[...,2] - K)/(1-K)

# Calculate M
M = (1-bgrdash[...,1] - K)/(1-K)

# Calculate Y
Y = (1-bgrdash[...,0] - K)/(1-K)
test=range(0,width)
print(f"width X height = {width} X {height}")
textFile = open('out1.prn', 'w')
with open('out1.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    #<class 'numpy.ndarray'> K/C/M/Y data type
    for row in range(0,height):
        tempK = np.full((width), 255.0)
        tempC = np.full((width), 255.0)
        tempM = np.full((width), 255.0)
        tempY = np.full((width), 255.0)
        #print(f"={K[row]}, {C[row]}, {M[row]}, {Y[row]}=\n\n\n\n")
        tList = np.concatenate((K[row],C[row], M[row],Y[row]))
        write.writerow(tList)
        
        tempK *= K[row]
        tempC *= C[row]
        tempM *= M[row]
        tempY *= Y[row]
        tList = np.concatenate((tempK,tempC, tempM, tempY)).astype(int)
        #tList = np.vectorize(hex)(tList) 
        write.writerow(tList)
        #textFile.write(tList)
        tList.astype('int8').tofile(textFile)
        #np.savetxt(textFile, tList,fmt='%X', delimiter='', newline='')
        
        #write.writerow(K[row]) 
        #write.writerow(C[row]) 
        #write.writerow(M[row]) 
        #write.writerow(Y[row])
        #print(f"List = {tList}")
        print(f"Processed Row#{row}")
    #for col in range(0,width):
    #    print(f"={K[row][col]}= ")
        
#   python3 cymk1.py
# Combine 4 channels into single image and re-scale back up to uint8
# CMYK = (np.dstack((C,M,Y,K))*255).astype(np.uint8)
# cv2.imwrite("CMYK.jpg", CMYK)