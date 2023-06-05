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

import cv2
import numpy as np
def find_contour(img):
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
    cv2.imwrite('D:/contours.png',img_contours)
    return

while not done:
    env.render()

    action = env.action_space.sample()

    action = default_policy()
    screen, reward, done, info = env.step(action)
    find_contour(screen)
    print("Action", action)
    print("image ", screen.shape, "reward ", reward, "Done?", done)
    print("Info", info)