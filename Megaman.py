import retro
import random
env = retro.make(game='MegaMan2-Nes')

env.reset()

done = False


frame_count_shooting = 0
frame_count_jumping = 0
def default_policy():
    #[shoot, dunno, dunno, up?, down?, left, right, jump]
    default_policy = [0, 0, 0, 0, 0, 0, 0, 1, 0]
    global frame_count_shooting, frame_count_jumping
    frame_count_shooting += 1
    if (frame_count_shooting == 10):
        frame_count_shooting = 0
        default_policy[0] = 1

    frame_count_jumping += 1
    if (frame_count_jumping > 30):
        default_policy[-1] = 1
    if (frame_count_jumping == 60):
        frame_count_jumping = 0

    return default_policy

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

import cv2
import numpy as np
def find_contour(img):
    
    img = repeat_upsample(img, 2, 2)
    img = repeat_upsample(img, 2, 2)

    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    cv2.imshow('bruh1', img)

    img = cv2.GaussianBlur(img,(11,11),cv2.BORDER_DEFAULT)
    # cv2.imshow('blurred', img)
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
    cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
    #save image
    cv2.imwrite('D:/contours.png', img_contours)
    cv2.imshow('bruh', img_contours)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img_contours

while not done:
    env.render()

    action = env.action_space.sample()

    action = default_policy()
    screen, reward, done, info = env.step(action)
    
    rgb = env.render('rgb_array')
    contour = find_contour(rgb)
    
    contour = cv2.resize(contour, rgb.shape[:-1])
    cv2.imshow('final', contour)
    cv2.waitKey(0)
    print("Action", action)
    print("image ", contour.shape, "reward ", reward, "Done?", done)
    print("Info", info)