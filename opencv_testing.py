import numpy as np
import cv2

class classify_zone:
    def __init__(self, start_point, end_point, color, thickness):
         self.start_point = start_point
         self.end_point = end_point
         self.color = color
         self. thickness = thickness

start_point = (10, 5) 
end_point = (220, 215) 
color = (255, 0, 0)
thickness = 2
zone1 = classify_zone(start_point, end_point, color, thickness)

start_point = (400, 5) 
end_point = (620, 220) 
color = (255, 0, 0)
thickness = 2
zone2 = classify_zone(start_point, end_point, color, thickness)


def draw_rects(image):
    rect1 = cv2.rectangle(image, zone1.start_point, zone1.end_point, zone1.color, zone1.thickness)
    rect2 = cv2.rectangle(rect1, zone2.start_point, zone2.end_point, zone2.color, zone2.thickness)
    
    return rect2


def start_video():
    
    cap = cv2.VideoCapture(0)
    
    processing_img = False
    
    while(True):
    
        key = cv2.waitKey(1)
        
        ret, frame = cap.read()
        resize = cv2.resize(frame, (640, 480), interpolation = cv2.INTER_LINEAR)  #resize window
        
        if key == ord('q'):
            break
        
        if key == ord('a') and processing_img is False:
            grayscale = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY) #greyscale image
            cv2.imwrite("frame%d.jpg" % 0, grayscale) 
            print("Processing image")
            processing_img = True
            #Do image processing here and send somewhere
            img = cv2.imread("frame0.jpg")
            crop_img = img[zone1.start_point[0] : zone1.end_point[0], zone1.start_point[1] : zone1.end_point[1]].copy()
            cv2.imshow("cropped", crop_img)
            processing_img = False
            
        final = draw_rects(resize) #add rectangles
        cv2.imshow("frame", final)
    
    
    cap.release()
    cv2.destroyAllWindows()


def main(): 
    start_video()

if __name__== "__main__":
  main()

#
#import cv2
#import matplotlib.pyplot as plt
#import cvlib as cv
#from cvlib.object_detection import draw_bbox
#
#
#im = cv2.imread('images/hand.jpg')
#bbox, label, conf = cv.detect_common_objects(im)
#output_image = draw_bbox(im, bbox, label, conf)
#plt.imshow(output_image)
#plt.show()

# Have a section on the screen that is set to where your hand should go
# then we have a timer that goes down and takes a snapshot of the hand 


#How to crop an image with opecv
#https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
    #Maybe show user their camera but feed our classifiers the cropped images

#maybe take multiple images after the timer goes down?