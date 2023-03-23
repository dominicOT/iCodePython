#mini VA properties

import cv2 #cv2.videocapture() to get video capture object for the camera

#.#.#.#.#.##.#.#..#..#.#start video recording with camera
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read() #capture vidreo frame by frame

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):  #x is set as the quitting button
        break

vid.release() #release the captured object
cv2.destroyAllWindows() #destroy all windows

