from keras.models import load_model
import numpy as np
import sys 
import os
#TODO: #Is there a better way to do this??
#sys.path.append(os.path.abspath("..")) #Some python directory stuff we can do to access files
from lib import video_processor

#TODO: How can we solve this pathing issue?
#This path will be relative to if you call from the game or from prediction_driver

def get_prediction():
    f = load_model('classifiers/CNNmodel.h5')
    
    image = video_processor.process_img()
    
    return model_prediction(f, image)

def model_prediction(model, image):
    data = np.asarray( image, dtype="int32" )
    
    pred_probab = model.predict(data)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class


def main(): 
    get_prediction()

if __name__== "__main__":
  main()