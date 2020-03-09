from keras.models import load_model
import numpy as np

from lib import video_processor

f = load_model('CNNmodel.h5')

input = video_processor.process_img()

im4 = np.resize(input, (28, 28, 1))
im5 = np.expand_dims(im4, axis=0)

#print(im5)

def model_prediction(model, image):
    data = np.asarray( image, dtype="int32" )
    
    pred_probab = model.predict(data)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class

print(model_prediction(f, im5))
