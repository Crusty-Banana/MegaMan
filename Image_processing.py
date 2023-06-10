import cv2
import numpy as np
from QLearning import *
Megaman_img1 = np.array([[1, 0, 0],
                        [1, 0, 0],
                        [1, 0, 1],
                        [0, 1, 0]])

Megaman_img2 = np.array([[0, 0, 1],
                        [0, 0, 1],
                        [1, 0, 1],
                        [0, 1, 0]])
Black =  np.array([0, 0, 0])
Blue = np.array([248, 228, 160])
last_y_pos = 0

def find_megaman(img):
    rows, column = img.shape[:2]
    tmp = repeat_upsample(img, 4, 4)
    cv2.imshow("masked", tmp)
    cv2.waitKey(0)
    global last_y_pos
    for y in range(rows - 3):
        for x in range(column - 2):
            flag = True
            for i in range(3):
                for j in range(2):
                    if (Megaman_img1[i, j] == 1):
                        if (img[y + i, x + j] == Black).all():
                            flag = False
                    else:
                        if (img[y + i, x + j] == Blue).all():
                            flag = False
            if (flag == True):
                last_y_pos = rows - y
                print(last_y_pos)
                return rows - y
            ``
            flag = True
            for i in range(3):
                for j in range(2):
                    if (Megaman_img2[i, j] == 1):
                        if (img[y + i, x + j] == Black).all():
                            flag = False
                    else:
                        if (img[y + i, x + j] == Blue).all():
                            flag = False
            if (flag == True):
                last_y_pos = rows - y
                print(last_y_pos)
                return rows - y
            
    return last_y_pos

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
    img = img[:,(xPos - 20):(xPos + 3)]
    
    masked = get_mask(img, (248, 228, 160))
    return find_megaman(masked)

def get_current_state(env, button_pressed):
    screen, reward, done, info = env.step(button_pressed)

    rgb = env.render('rgb_array')
    
    yPos = find_yPos(rgb, info['xPos'])

    current_state = State(info['progress'], yPos, info['health'])

    return screen, reward, done, current_state
