import numpy as np
import cv2

class classify_zone:
    def __init__(self, start_point, end_point, color, thickness):
         self.start_point = start_point
         self.end_point = end_point
         self.color = color
         self. thickness = thickness
         
classifier_image_height = 28
classifier_image_width = 28

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


def process_img():
    print("Processing image")
    dim = (classifier_image_height, classifier_image_width) 
    # Read in the entire image
    img = cv2.imread("frame0.jpg")
    # Crop the image according to the bounding box on the game camera
    crop_img = img[zone1.start_point[0] : zone1.end_point[0], zone1.start_point[1] : zone1.end_point[1]].copy()
    # Grayscale the cropped image
    grayscale = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) 
    # Add GaussianBlur
    image_grayscale_blurred = cv2.GaussianBlur(grayscale, (15,15), 0)
    # Resize according to what classifier was tried on (right now 28 by 28)
    resized = cv2.resize(image_grayscale_blurred, dim, interpolation = cv2.INTER_AREA)
    # Write the image to file (just for debugging)
    cv2.imwrite("resized_img.jpg", resized) 
    
    im4 = np.resize(resized, (28, 28, 1))
    im5 = np.expand_dims(im4, axis=0)
    
    print("Image processed")
    #TODO: Figure out how we want to do this pipelining
#    return resized
    return im5

def start_video(cap):
    key = cv2.waitKey(1)
    
    ret, frame = cap.read()
    resize = cv2.resize(frame, (640, 480), interpolation = cv2.INTER_LINEAR)  #resize window
    
    
    if key == 27:
        return None, None
    
    final = draw_rects(resize) #add rectangles
    cv2.imshow("frame", final)
    
    return ret, resize
    
def write_image(frame):
     cv2.imwrite("frame%d.jpg" % 0, frame)
     print("Image captured")
    
def end_video(cap):
    cap.release()
    cv2.destroyAllWindows()

def main(): 
    start_video()

if __name__== "__main__":
  main()

#How to crop an image with opecv
#https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
