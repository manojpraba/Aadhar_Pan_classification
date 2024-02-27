import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from cnnClassifier import logger
#from cnnClassifier.OCR.aadhar_deatils import Aadhar_extract as ad
#from cnnClassifier.OCR.pan_details import pan_extract as pd
from cnnClassifier.OCR.OCR_pytessreact.pytess_main import pytess_main1 as pm

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
        value=model.predict(test_image)
        print("original",model.predict(test_image))
        print("This is the prediction value",value[0][0],"and",value[0][1])
        print("==============================")
        logger.info(f"This is the prediction value {value[0][0]} and {value[0][1]}")
                    
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)
        try:
            if result[0] == 1:
                prediction = 'AADHAR'
                details=pm(imagename,prediction)
                
                values=details.test()
                #values=pd(imagename)
                #return [values.extract()]
                return [values]
           
            else:
                prediction = 'PAN'
                details=pm(imagename,prediction)
                
                values=details.test()
                #values=pd(imagename)
                #return [values.extract()]
                return [values]
        except Exception as e:
            logger.exception(e)
            
            return [{ "image" : e}]
           
        
        