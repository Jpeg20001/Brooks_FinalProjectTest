# David Brown, Michael Gonzales
# brown6dw@mail.uc.edu"
# Final Project"
# 11/29/2023
# IS 4010
# Fall 2023
# The project shows I can use AI to help solve arrays and other fun stuff.

from jsonReaderPackage.jsonReader import *
from TxtExtractorPackage.TxtExtractorClass import *

import json

if __name__ == "__main__":

    
    json_reader = JsonDataReader('EncryptedGroupHints Fall 2023 Section 001.json')

    json_reader.read_data()

    data = json_reader.get_data()
    
    intBrooksNumbers = [int(num) for num in data]

    # Txt File processing 
    txt_extractor = TextFileExtractor('english-2.txt')
    txt_extractor.read_lines()
    result = txt_extractor.extract_info_by_indexes(intBrooksNumbers)
    print(result)
    
