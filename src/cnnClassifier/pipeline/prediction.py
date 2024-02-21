import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from cnnClassifier import logger


class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("trained_model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)
        try:
            if result[0] == 1:
                prediction = 'Aadhar CARD'
                return [{ "image" : prediction}]
            else:
                prediction = 'PAN CARD'
                return [{ "image" : prediction}]
        except Exception as e:
            logger.exception(e)
            
            return [{ "image" : e}]
           
        
        