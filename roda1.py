import numpy as np
import cv2
import time
from collections import deque
import numpy as py
import RPi.GPIO as GPIO
import socket

GPIO.setmode(GPIO.BCM)  # set pi to use pin number when referencing GPIO pins
                        # can use GPIO.setmode(GPIO.BCM) instead to use
                        # Broadcom SOC channel names
GPIO.setwarnings(False)


GPIO.setup(20, GPIO.OUT)    # set motor kiri
GPIO.setup(21, GPIO.OUT)    # set motor

GPIO.setup(19, GPIO.OUT)    # set motor kanan
GPIO.setup(26, GPIO.OUT)    # set motor

GPIO.setup(5, GPIO.OUT)    # set motor belakang
GPIO.setup(6, GPIO.OUT)    # set motor

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)    # set penendang

Ena, In1, In2 = 17, 27, 22 # penggiring
Enb, In3, In4 = 10, 9, 11

GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)




pwm_1a = GPIO.PWM(20, 100)  # initialize PWM on pwmPin to 100 Hz freq
pwm_1b = GPIO.PWM(21, 100)

pwm_2a = GPIO.PWM(19, 100)
pwm_2b = GPIO.PWM(26, 100)

pwm_3a = GPIO.PWM(5, 100)
pwm_3b = GPIO.PWM(6, 100)

pwm_4a = GPIO.PWM(2, 100)
pwm_4b = GPIO.PWM(3, 100)

pwm1 = GPIO.PWM(Ena, 100)
pwm2 = GPIO.PWM(Enb, 100)


dc = 0      # variable for setting the duty cycle
pwm_1a.start(dc)
pwm_1b.start(dc)
pwm_2a.start(dc)
pwm_2b.start(dc)
pwm_3a.start(dc)
pwm_3b.start(dc)
pwm_4a.start(dc)
pwm_4b.start(dc)
pwm1.start(0)
pwm2.start(0)


def maju_motor():
    pwm_1a.ChangeDutyCycle(30)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(30)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(0)
#     pwm_4a.ChangeDutyCycle(0)
#     pwm_4b.ChangeDutyCycle(10)
#     pwm1.ChangeDutyCycle(20)
#     pwm2.ChangeDutyCycle(20)


def maju_motor_awal():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(5)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(5)
    pwm_3b.ChangeDutyCycle(0)
# 
# def penggiring():
#     GPIO.output(In1, GPIO.LOW)
#     GPIO.output(In2, GPIO.HIGH)
# 
#     GPIO.output(In3, GPIO.HIGH)
#     GPIO.output(In4, GPIO.LOW)
#     pwm1.ChangeDutyCycle(20)
#     pwm2.ChangeDutyCycle(20)

    # GPIO.cleanup()    # wait .05 sec at current LED brightness
    # time.sleep(0.5)

def mundur_motor():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(5)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(5)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(0)

def stop_motor():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(0)

def putar_kanan():
    pwm_1a.ChangeDutyCycle(5)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(5)
    pwm_3a.ChangeDutyCycle(5)
    pwm_3b.ChangeDutyCycle(0)

def min_putar_kanan():
    pwm_1a.ChangeDutyCycle(5)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(5)
    pwm_3a.ChangeDutyCycle(5)
    pwm_3b.ChangeDutyCycle(0)

def putar_kiri():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(10)
    pwm_2a.ChangeDutyCycle(10)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(10)

def min_putar_kiri():
    pwm_1a.ChangeDutyCycle(0) #searah jarum jam(a)
    pwm_1b.ChangeDutyCycle(5) #berlawanan jarum jam(b)
    pwm_2a.ChangeDutyCycle(5)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(5)

def putar_kiri_awal():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(10)
    pwm_2a.ChangeDutyCycle(10)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(10)

def max_putar_kiri():
    pwm_1a.ChangeDutyCycle(0)
    pwm_1b.ChangeDutyCycle(5)
    pwm_2a.ChangeDutyCycle(5)
    pwm_2b.ChangeDutyCycle(0)
    pwm_3a.ChangeDutyCycle(0)
    pwm_3b.ChangeDutyCycle(5)

def max_putar_kanan():
    pwm_1a.ChangeDutyCycle(5)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(5)
    pwm_3a.ChangeDutyCycle(5)
    pwm_3b.ChangeDutyCycle(0)

def putar_kanan_awal():
    pwm_1a.ChangeDutyCycle(5)
    pwm_1b.ChangeDutyCycle(0)
    pwm_2a.ChangeDutyCycle(0)
    pwm_2b.ChangeDutyCycle(5)
    pwm_3a.ChangeDutyCycle(5)
    pwm_3b.ChangeDutyCycle(0)



# def kanan():
#     pwm_1a.ChangeDutyCycle(3)
#     pwm_1b.ChangeDutyCycle(0)
#     pwm_2a.ChangeDutyCycle(30)
#     pwm_2b.ChangeDutyCycle(0)
#     pwm_3a.ChangeDutyCycle(32)
#     pwm_3b.ChangeDutyCycle(0)
# 
# def kiri():
#     pwm_1a.ChangeDutyCycle(0)
#     pwm_1b.ChangeDutyCycle(7)
#     pwm_2a.ChangeDutyCycle(0)
#     pwm_2b.ChangeDutyCycle(30)
#     pwm_3a.ChangeDutyCycle(0)
#     pwm_3b.ChangeDutyCycle(30)
    
# define the lower and upper boundaries of the "orange" color in the HSV color space
orange_lower = np.array([5, 50, 50])
orange_upper = np.array([15, 255, 255])

# start the video capture
cap = cv2.VideoCapture(0)
try:
    while True:
        # read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # resize the frame to a smaller size for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # convert the frame to the HSV color space
        hsv = cv2.cvtColor(small_frame, cv2.COLOR_BGR2HSV)

        # threshold the HSV image to get only orange colors
        mask = cv2.inRange(hsv, orange_lower, orange_upper)

        # apply a series of dilations and erosions to the mask using an elliptical kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.erode(mask, kernel, iterations=2)
        mask = cv2.dilate(mask, kernel, iterations=2)

        # find contours in the mask and initialize the current (x, y) center of the orange object
        cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None
        

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                       
            #print("radius", radius)
            print("nilai x", x)
            print("nilai y", y)
            
            #gerak_roda_mencari_bola
            if x > 190 and x < 210: #if x == y
                maju_motor()
                print("maju")
                
            elif y > 180 and y < 210:
                stop_motor()
                print("stop")
#             elif x > 215 and x < 286:
#                   min_putar_kiri()
#                   print("Kiri 1")
            #elif y > 78 and y < 80
             #   stop_motor()
#                  time.sleep(0.2)
#                  stop_motor()
#                  print("stop")
#             elif x > 254 and x < 286:
#                  min_putar_kiri()
#                  print("Kiri 2")
#                  time.sleep(0.2)
#                  stop_motor()
#                  print("stop")
#             elif x > 110 and x < 195:
#                  min_putar_kanan()
#                  print("Kanan 1")
#                  time.sleep(0.2)
#                  stop_motor()
#                  print("stop")
#             elif x > 150 and x < 195:
#                  min_putar_kanan()
#                  print("Kanan 2")
#                  time.sleep(0.2)
#                  stop_motor()
#                  print("stop")
            else:
                 stop_motor()
            
            #
            

            # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # and update the list of tracked points
                cv2.circle(frame, (int(x*2), int(y*2)), int(radius*2), (0, 255, 255), 2)
                cv2.circle(frame, (int(center[0]*2), int(center[1]*2)), 5, (0, 0, 255), -1)

        # show the frame
        

        # create a black frame to use as a background for text
        black_frame = np.zeros((frame.shape[0]+200, frame.shape[1], 3), dtype=np.uint8)
        black_frame[100:frame.shape[0]+100, :] = (0, 0, 0)

        # Combine the frame with the black frame
        frame_with_black = cv2.vconcat([black_frame, frame])

        # Convert the frame from BGR to HSV
        hsv_frame = cv2.cvtColor(frame_with_black, cv2.COLOR_BGR2HSV)

        # Threshold the HSV image to get only orange colors
        mask = cv2.inRange(hsv_frame, orange_lower, orange_upper)

        # Find contours in the thresholded image
        # find contours in the thresholded image
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # initialize the contour color and the current (x, y) center of the orange object
        contour_color = (255, 0, 0)
        center = None

        # loop over the contours
        for contour in contours:
            # find the area of the contour
            area = cv2.contourArea(contour)

            # only proceed if the area is above a certain threshold
            if area > 100:
                # find the perimeter of the contour
                perimeter = cv2.arcLength(contour, True)

                # approximate the contour as a polygon
                approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)

                # find the center of the polygon
                M = cv2.moments(approx)
                if M["m00"] != 0:
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
            

                # draw the contour and center on the frame,
                # and update the list of tracked points
                cv2.drawContours(frame_with_black, [approx], 0, contour_color, 2)
                if center is not None:
                    cv2.circle(frame_with_black, center, 5, (0, 0, 255), -1)

        # show the frame
        cv2.imshow("Frame", frame)
        
        
    #     cv2.imshow("Frame", frame_with_black)

        # wait for a key press
        key = cv2.waitKey(1) & 0xFF

        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break
        
        
    # release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

except KeyboardInterrupt:
    stop_motor()

#condition

