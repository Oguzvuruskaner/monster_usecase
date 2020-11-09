import cv2
import os
from random import randint,random

from get_whitened_image import get_whitened_image

VID_HEIGHT = 480
VID_WIDTH = 640

anomaly_happen = lambda: random() < 1e-1

get_random_top_offset = lambda: randint(0,200)
get_random_left_offset = lambda : randint(350,450)
get_random_frame_size = lambda : randint(35,48)


if __name__ == "__main__":

    vid = cv2.VideoCapture(0)

    monster = cv2.imread(os.path.join("images","monster_with_alpha.png"))
    monster = get_whitened_image(monster)
    monster = monster[::5,::5]

    anomaly_frame = 0
    delta = [0,0]
    current = [0,0]

    while (True):


        ret, frame = vid.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2RGBA)

        if anomaly_frame > 0:
            current[0] += delta[0]
            current[1] += delta[1]
            frame[int(current[0]):int(current[0])+monster.shape[0],
                int(current[1]):int(current[1])+monster.shape[1]] *= (255-monster[:,:,3:4])//255
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            frame[int(current[0]):int(current[0]) + monster.shape[0],
            int(current[1]):int(current[1]) + monster.shape[1]] += (monster[:,:,3:4])//255 * monster

            anomaly_frame -= 1

        elif anomaly_happen():
            anomaly_frame = get_random_frame_size()
            current = [get_random_top_offset(),get_random_left_offset()]
            delta = [
                (get_random_top_offset()-current[0])/anomaly_frame,
                (get_random_left_offset() - current[1])/anomaly_frame ]


        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
