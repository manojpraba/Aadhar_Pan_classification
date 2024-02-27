from cnnClassifier.OCR.ocr_main import reader
import re
from cnnClassifier import logger
from collections import OrderedDict
class pan_extract:
    def __init__(self,img_path) -> None:
        self.img_path=img_path
    def extract(self):
       
       
        img_path1 = 'C:/DL projects/Aadhar_Pan_classification/aadhar.jpg'

        # Perform text detection and recognition
        try:
            result = reader.readtext(self.img_path)
            name = None
            pan_number = None
            dob = None
            values=OrderedDict()
            values['Type :']="PAN CARD"
            # Regular expression patterns
            name_pattern = r"^[A-Z\s]+"
            pan_number_pattern = r"[A-Z]{5}[0-9]{4}[A-Z]"
            dob_pattern = r"(\d{2}/\d{2}/\d{4})"
        
            for tup in result:
                # Extract string value from the tuple
                string_value = tup[1]
                
                # Check if the string value matches the regular expression patterns
                if not name and re.match(name_pattern, string_value):
                    name = string_value.strip()
                    values['Name :']=name
                
                elif not pan_number and re.match(pan_number_pattern, string_value.replace(" ", "")):
                    pan_number = string_value
                    values['Pan Number :']=pan_number
                elif not dob:
                    dob_match = re.search(dob_pattern, string_value)
                    if dob_match:
                        dob = dob_match.group(1)
                        values["Date of Birth:"]= dob
            print("Name:", name)
            print("Pan Number:", pan_number)
            print("Date of Birth:", dob)
            return values
        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ =='__main__':
    ad=pan_extract('C:/DL projects/Aadhar_Pan_classification/aadhar.jpg')
    ad.extract()             

        
