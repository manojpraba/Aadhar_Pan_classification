import cv2
import pytesseract
from pathlib import Path
import spacy
import numpy as np
import re, os, time, json
from pathlib import Path
from collections import OrderedDict
from cnnClassifier import logger

class pytess_main1:
    def __init__(self,aadhaar_front_img_path,img_type):
        self.aadhaar_front_img_path=aadhaar_front_img_path
        self.img_type=img_type
        


    def test(self):
        try:
        
            tesseract_path = Path(r"C:\DL projects\tess\tesseract.exe")
            #self.aadhaar_front_img_path = Path(r"C:\Users\mmanoj\Desktop\AAdhar card\aadhar_card_full.jpg")
            
            aadhaar_back_img_path = Path("<path/to/aadhaar_back_image>")
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
            # Path to aadhaar front image
            try:

                img = cv2.imread(self.aadhaar_front_img_path)
                # Resize image (fx=0.5,fy=0.5 is half the original size)
                img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
            except Exception as e:
                logger.exception(e)
                print(e)

            four_points = []
            # getting all values (except address) from Front Aadhaar Card Image
            if self.img_type=="AADHAR":

                regex_name,regex_gender,regex_dob,regex_aadhaar_number = self.get_values(img)
                regex_name = " ".join(regex_name)
                values=OrderedDict()
                values["TYPE "]="AADHAR"
                values['NAME ']=regex_name
                values['GENDER ']=regex_gender
                values['DOB ']=regex_dob
                values['AADHAR NUMBER ']=regex_aadhaar_number
                print(regex_name,regex_gender,regex_dob,regex_aadhaar_number)
                return values
            else:
                regex_name,regex_dob,regex_pan_number =self.get_values_pan(img)
                regex_name = " ".join(regex_name)
                values=OrderedDict()
                values["TYPE "]="PAN CARD"
                values['NAME ']=regex_name
                values['DOB ']=regex_dob
                values['PAN NUMBER ']=regex_pan_number
                print(regex_name,regex_dob,regex_pan_number)
                return values
        except Exception as e:
            logger.exception(e)
            print(e)


            
            



    def get_values(self,img):
    
        regex_name = None
        regex_gender = None
        regex_dob = None
        
        regex_aadhaar_number = None
        #Name Entity Recognition function
        NER = spacy.load("en_core_web_sm")
        
        thresh =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2str_config_name = "--psm 4 --oem 3"
        res_string_name = pytesseract.image_to_string(thresh,lang='eng',config=img2str_config_name)
        name=NER(res_string_name)

        #extracting name
        for word in name.ents:
            if word.label_ == "PERSON":
                regex_name  = re.findall("[A-Z][a-z]+", word.text)
        if not regex_name:
            regex_name = re.findall("[A-Z][a-z]+", res_string_name)
        #print(res_string_name)

        #extracting information other than name
        img2str_config_else = "--psm 3 --oem 3"
        res_string_else = pytesseract.image_to_string(thresh,lang='eng',config=img2str_config_else)
        

        if not regex_name:
            regex_name = re.findall("[A-Z][a-z]+", res_string_else)
        #extracting gender
        if not regex_name:
            regex_name="NA"
        regex_gender = re.findall("MALE|FEMALE|male|female|Male|Female", res_string_else)
        if regex_gender:
            regex_gender = regex_gender[0]
        #print(regex_gender)

        #extracting date of birth
        regex_aadhaar_number = re.findall(r'\d{4}\s?\d{4}\s?\d{4}'
,res_string_else)
        if regex_aadhaar_number:
            regex_aadhaar_number = regex_aadhaar_number[0]

        regex_dob = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', res_string_else)
        if regex_dob:
            regex_dob = regex_dob[0]
        #print("dob1",regex_dob)
        if not regex_dob:
            regex_dob = re.findall("\d{1,2}\/\d{1,2}\/\d{2,4}", res_string_else)
        if not regex_dob:
            regex_dob="NA"
        
        return(regex_name,regex_gender,regex_dob,regex_aadhaar_number)
    
    def get_values_pan(self,img):
   
        regex_name = None
        
        regex_dob = None
        
        regex_pan_number = None
        #Name Entity Recognition function
        NER = spacy.load("en_core_web_sm")
        
        thresh =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2str_config_name = "--psm 4 --oem 3"
        res_string_name = pytesseract.image_to_string(thresh,lang='eng',config=img2str_config_name)
        name=NER(res_string_name)

        #extracting name
        for word in name.ents:
            if word.label_ == "PERSON":
                regex_name  = re.findall("[A-Z ]", word.text)
                print("first",regex_name)
        
        if not regex_name:
             regex_name=re.findall(r"^[A-Z\s]+",res_string_name)
        
               
        #extracting information other than name
        img2str_config_else = "--psm 3 --oem 3"
        res_string_else = pytesseract.image_to_string(thresh,lang='eng',config=img2str_config_else)
        
        if not regex_name:
             regex_name  = re.findall("[A-Z ]", res_string_else)
        if not regex_name:
            regex_name="NA"
        

       
        regex_dob = re.findall("\d{2}/\d{2}/\d{4}", res_string_else)
        if regex_dob:
            regex_dob = regex_dob[0]
        #print("dob1",regex_dob)
        if not regex_dob:
            regex_dob = re.findall("(\d\d\d\d){1}", res_string_else)
        if not regex_dob:
            regex_dob="NA"
        regex_pan_number = re.findall("[A-Z]{5}[0-9]{4}[A-Z]",res_string_else)
        if regex_pan_number:
            regex_pan_number = regex_pan_number[0]
        #print(regex_aadhaar_number)

        return(regex_name,regex_dob,regex_pan_number)

if __name__ == '__main__':
    pym=pytess_main("C:\DL projects\Aadhar_Pan_classification\inputImage.jpg","AADHAR")
    pym.test()
