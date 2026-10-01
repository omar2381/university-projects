import os
import math
import cv2
import numpy as np


def val_correction(words,default_val,minimum,maximum):
    try:
        value = float(input("%s (%1.2f-%1.2f) [%1.2f]: " %(words,minimum,maximum,default_val)))
        if ((value >= minimum) and (value <= maximum)): #checks to make sure the entered value is within the required limit
            return value  # if it is in the limit, the vlue is unchanged
        else:
            print("value is out of range")
            return default_val #if the value is incorrect, the default value is returned
    except ValueError:
        print("Value is incorrect")
        return default_val 

def make_gray(img):
    rows,cols,channels = img.shape
    grayimg = np.full((rows, cols, channels), 0, np.uint8)
    for i in range(rows):
        for j in range(cols):
            a = 0.07 * img[i,j][0]
            b = 0.72 * img[i,j][1]
            c = 0.21 * img[i,j][2]
            grayimg[i,j] = a + b + c 
    return grayimg

def make_noise(img):
    img = np.full((rows, cols, channels), 0, np.uint8)
    for x in range(rows): 
        for y in range(cols):
            p = np.random.uniform(0.0, 1.0)     
            if p < probabilty/2:
                img[x,y,:] = (255,255,255)    
            elif p < probabilty:
                img[x,y,:] = (0,0,0)
    return img

def blur(img,n):
    imgNew = np.zeros((rows, cols, channels))
    for x in range(n, rows-n):          
        for y in range(n, cols-n):      
            for z in range(channels):   
                neighbourhood = img[x-n:x+n, y-n:y+n, z]    
                imgNew[x,y,z] = np.median(neighbourhood)
    return imgNew

def normal(img):
    bigtable = np.array([ i*1.25 for i in range (0,256)]).clip(0,255).astype('uint8')
    smoltable = np.array([ i/1.25 for i in range (0,256)]).clip(0,255).astype('uint8')
    b,g,r = cv2.split(img)
    r = cv2.LUT(r,bigtable)
    b = cv2.LUT(b,smoltable)
    img = cv2.merge((b,g,r))
    return img

def motionblur(img):
    k = np.zeros((kernel_size, kernel_size)) 
    k[int((kernel_size - 1)/2), :] = np.ones(kernel_size)  
    k /= kernel_size  
    horizonal_img = cv2.filter2D(img, -1, k) 
    return horizonal_img

def problem1(mode,img):
    while mode != 's' and mode != 'r':
        mode = input("\nyou have entered an invalid mode, please enter either an s for Simple or r for Rainbow: ")

    darkening_coefficient = val_correction("\nslect the darkening coefficient:",0.6,0.0,1.0)
    blending_coefficient  = val_correction("\nslect the blending coefficient:",0.4,0.0,1.0)

    if mode == 's':
        mask = cv2.imread('./mask.jpg')
        img = (img * blending_coefficient + mask * (1 - blending_coefficient)) * darkening_coefficient
        cv2.imwrite("light_ray.jpg", img)
    elif mode == 'r':
        mask = cv2.imread('./rainbowmask.jpg')
        img = (img * blending_coefficient + mask * (1 - blending_coefficient)) * darkening_coefficient
        cv2.imwrite("Rainbow.jpg", img)
    input("press enter to continue")

def problem2(mode,img):
    while mode != 'm' and mode != 'c':
        mode = input("\nyou have entered an invalid mode, please enter either an m for Monochrome or c for Coloured Pencil: ")

    if mode == 'm':
        blending_coefficient  = val_correction("\nslect the blending coefficient:",0.4,0.0,1.0)
        gray = make_gray(img)
        noise = make_noise(img)
        horizonal = motionblur(noise)
        img = horizonal * (1.0 - blending_coefficient) + gray * blending_coefficient
        cv2.imwrite("Mono.jpg", img)

    elif mode == 'c':
        salt = make_noise(img)
        pepper = make_noise(img)
        salt = motionblur(salt)
        pepper = motionblur(pepper)

        b, g, r = cv2.split(img)
        bs,gs,rs = cv2.split(salt)
        bp,gp,rp = cv2.split(pepper)
        b = bp
        g = gs
        r = r 
        img = cv2.merge((b,g,r))

        cv2.imwrite("Coloured.jpg", img)
    input("press enter to continue")

def problem3(img):
    blurring_amount = int(val_correction("\nslect the blurring amount:",2,0,8))
    img = normal(img)
    img = blur(img,blurring_amount)
    cv2.imwrite("beautified.jpg", img)
    input("press enter to continue")

def rotate (i,j,radius,swirl_angle,centre_y,centre_x):
    y = i - centre_x
    x = j - centre_y
    r = math.sqrt((x**2) + (y**2))

    theta = math.atan2(x,y)

    swirlAmount = 1-(r/radius)
    if swirlAmount > 0:
        total = swirlAmount * swirl_angle * math.pi * 2.0
        theta += total
        y = int(math.cos(theta) * r)
        x = int(math.sin(theta) * r)
    return x+centre_x , y+centre_y

def problem4(img):
    swirl_angle = val_correction("enter the swirl strength: ",0.4,-4,4)
    swirl_radius = val_correction("enter the swirl radius: ",150,10,200)

    newimg = np.zeros((rows, cols, channels))
    centre_x = int(rows/2)
    centre_y = int(cols/2)

    for i in range(0,cols):
        for j in range(0,rows):
            y,x = rotate(i,j,swirl_radius,swirl_angle,centre_y,centre_x)
            newimg[i][j] = img[x][y]

    cv2.imwrite("Swirl.jpg", newimg)
    input("press enter to continue")


# define some variables
menu_choice = ""          #sets the inital choice

#images
img1 = cv2.imread('face1.jpg')
img2 = cv2.imread('face2.jpg')
rows,cols,channels = img1.shape

img = img1
image_type = 1

#problem 1 default parameters
mode = ""
darkening_coefficient = 0.5
blending_coefficient  = 0.4

lightbg = cv2.imread('light.png')
rainbowbg = cv2.imread('rainbow.png')

#problem 2 default parameters
probabilty = 0.4
kernel_size = 15

#problem 3 default parameters
blurring_amount = 0

#problem 4 default parameters
swirl_radius = 0
swirlTwists = 45


#main function 
while (menu_choice != 'q'):
	
    os.system("cls")

    print("\n")

	# print menu choices
    print("Welcome, please Select a Problem")

    print("\n")
	
    print("Enter 1   for Problem 1               (Light Leak/Rainbow Leak)")
    print("Enter 2   for Problem 2                (Pencil/Charcoal Effect)")
    print("Enter 3   for Problem 3        (Smoothing & Beautifying Fliter)")
    print("Enter 4   for Problem 4                            (Face Swirl)")
    print("Enter 5   to use other image              (currently on image" + str(image_type) + ")")
    print("Enter q   to quit the program")
	
	
	# get menu choice
    menu_choice = input("\nenter your option here: ") 	
	
	
    if (menu_choice == '1'):
        mode = input("slect your mode (s for Simple and r for Rainbow) here: ")
        problem1(mode,img)

    elif (menu_choice == '2'):
        mode = input("slect your mode (m for Monochrome or c for Coloured Pencil) here: ")
        problem2(mode,img)

    elif (menu_choice == '3'):
        problem3(img)

    elif (menu_choice == '4'):
        problem4(img)

    elif (menu_choice == '5'):
        if image_type == 1:
            img = img2
            image_type = 2
            print("You have selected: IMAGE2")
        else:
            img = img1
            image_type = 1
            print("You have selected: IMAGE1")
        input("Press enter to continue")

