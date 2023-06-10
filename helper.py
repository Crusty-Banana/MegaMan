import cv2
import numpy as np
Megaman_img = np.array([[1, 0, 0],
                        [1, 0, 0],
                        [1, 0, 1],
                        [0, 1, 0]])
Black =  np.array([0, 0, 0])
def find_megaman(img):
    rows, column = img.shape[:2]
    for y in range(rows - 3):
        for x in range(column - 2):
            flag = True
            for i in range(3):
                for j in range(2):
                    if (Megaman_img[i, j] == 1):
                        if (img[y + i, x + j] == Black).all():
                            flag = False
            if (flag == True):
                return rows - y
    return -1

def repeat_upsample(rgb_array, k=1, l=1, err=[]):
    # repeat kinda crashes if k/l are zero
    if k <= 0 or l <= 0: 
        if not err: 
            print("Number of repeats must be larger than 0, k: {}, l: {}, returning default array!".format(k, l))
            err.append('logged')
        return rgb_array

    # repeat the pixels k times along the y axis and l times along the x axis
    # if the input image is of shape (m,n,3), the output image will be of shape (k*m, l*n, 3)

    return np.repeat(np.repeat(rgb_array, k, axis=0), l, axis=1)

def get_mask(img, color):
    #get_mask(img, (248, 228, 160))
    lower = np.array(list(color))
    upper = np.array(list(color))
    mask = cv2.inRange(img, lower, upper)
    masked = cv2.bitwise_and(img,img, mask=mask)
    return masked

def find_yPos(img, xPos):
    img = img[:,(xPos - 10):(xPos)]
    
    masked = get_mask(img, (248, 228, 160))
    cv2.imshow("masked", masked)
    cv2.waitKey(0)
    return find_megaman(masked)

def find_contour(img, xPos):
    img = repeat_upsample(img, 2, 2)
    img = repeat_upsample(img, 2, 2)

    #crop image
    img = img[:,(xPos*4 - 40):(xPos*4)]
    #megaman pos
    mask = get_mask(img, (248, 228, 160))
    cv2.imshow('masked', mask)
    #blur image
    img = cv2.GaussianBlur(img,(11,11),cv2.BORDER_DEFAULT)
    #convert img to grey
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #set a thresh
    thresh = 100
    #get threshold image
    ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
    #find contours
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #create an empty image for contours
    img_contours = np.zeros(img.shape)
    # draw the contours on the empty image
    cv2.drawContours(img_contours, contours, -1, (0,255,0), thickness=cv2.FILLED)
    #save image
    cv2.imwrite('D:/contours.png', img_contours)
    # cv2.imshow('bruh', img_contours)

    return img_contours