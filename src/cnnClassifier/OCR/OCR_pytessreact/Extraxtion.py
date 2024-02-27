


def get_values(img):
    
        regex_name = None
        regex_gender = None
        regex_dob = None
        regex_mobile_number = None
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
        regex_gender = re.findall("MALE|FEMALE|male|female|Male|Female", res_string_else)
        if regex_gender:
            regex_gender = regex_gender[0]
        #print(regex_gender)

        #extracting date of birth
        regex_dob = re.findall("\d\d/\d\d/\d\d\d\d", res_string_else)
        if regex_dob:
            regex_dob = regex_dob[0]
        #print("dob1",regex_dob)
        if not regex_dob:
            regex_dob = re.findall("(\d\d\d\d){1}", res_string_else)[0]
        #print("dob2",regex_dob)

        #extracting mobile no.
    

        #extracting aadhaar number
        regex_aadhaar_number = re.findall("\d\d\d\d \d\d\d\d \d\d\d\d",res_string_else)
        if regex_aadhaar_number:
            regex_aadhaar_number = regex_aadhaar_number[0]
        #print(regex_aadhaar_number)

        return(regex_name,regex_gender,regex_dob,regex_mobile_number,regex_aadhaar_number)
    
    def get_values_pan(img):
   
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
        

        #extracting information other than name
        img2str_config_else = "--psm 3 --oem 3"
        res_string_else = pytesseract.image_to_string(thresh,lang='eng',config=img2str_config_else)
        

    
        regex_dob = re.findall("\d\d/\d\d/\d\d\d\d", res_string_else)
        if regex_dob:
            regex_dob = regex_dob[0]
        #print("dob1",regex_dob)
        if not regex_dob:
            regex_dob = re.findall("(\d\d\d\d){1}", res_string_else)[0]
        regex_pan_number = re.findall("[A-Z]{5}[0-9]{4}[A-Z]",res_string_else)
        if regex_pan_number:
            regex_pan_number = regex_pan_number[0]
        #print(regex_aadhaar_number)

        return(regex_name,regex_dob,regex_pan_number)
